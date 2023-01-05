from typing import List, Optional
from pydantic import BaseModel, Field 
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends, HTTPException, Body
from server.app import set_coll
from db_routes.question import Question
from id_model import PyObjectId
from db_routes.users import get_current_user

#Can modularize path operations w/the API Router
router = APIRouter(tags=["sets"])

class Set(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    title: str
    username: Optional[str] 
    questions: List[Question]
    rating: float
    
    class Config:
        fields = {'id': '_id'}

class UpdateSet(BaseModel):
    title: Optional[str]
    username: Optional[str] 
    questions: Optional[List[Question]]
    rating: Optional[int]

@router.get("/sets")
async def get_all_sets(is_count: Optional[bool] = False):
    if is_count:
        return await set_coll.count_documents({})
    
    return await set_coll.find({}).to_list(length=None)

#Token Required Functions: via dependency on oauth2 password bearer through get_current_user function
@router.post("/set", response_model=Set)
async def create_set(newSet: Set = Body(...), user = Depends(get_current_user)) -> Set:
    newSet.username = user["username"]
    newSet = jsonable_encoder(newSet)

    set = await set_coll.insert_one(newSet)
    createdSet = await set_coll.find_one({"_id": set.inserted_id})
    return createdSet

@router.delete("/set/{set_id}")
async def delete_set(set_id: str, user = Depends(get_current_user)):
    set = await set_coll.delete_one({"_id": set_id})

    #set is of type pymongo.Results.DeleteResult, check pymongo doc for more info
    if set.deleted_count < 1:
        raise HTTPException(status_code=400, detail="This set could not be deleted. Please try again later")

    return {"msg": "Set successfully deleted!"}

@router.put("/set/{set_id}")
async def update_set(
    set_id: str, 
    set: UpdateSet = Body(...), 
    user = Depends(get_current_user)
):
    set = {k: v for k, v in set.dict().items() if v is not None}

    updated_set = await set_coll.update_one({"_id": set_id}, {"$set": set})
    #updated_set is of type pymongo.Results.UpdatedResult, check pymongo doc for more info on returned fields
    if updated_set.modified_count < 1: 
        raise HTTPException(status_code=400, detail="This set could not be updated. Please try again later")

    return {"msg": "Set was successfully updated!"}