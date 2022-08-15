from typing import List, Optional
from pydantic import BaseModel
from bson.objectid import ObjectId
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends, HTTPException, Body

#Can modularize path operations w/the API Router
router = APIRouter(tags=["sets"])

from server.collections_db.question import Question
#Field(...) is used to indicate a required field
class Set(BaseModel):
    title: str
    position: int
    username: Optional[str] 
    questions: List[Question]
    rating: int

import sys
sys.path.insert(0,"..")
from server.app import set_coll

#get_current_user is used for authorization: dependency on it ensures that only authenticated users can be serviced
from collections_db.users import get_current_user

@router.get("/sets", response_model=List[Set])
async def get_all_sets()->List[Set]:
    sets = await set_coll.find({},{'_id': 0}).to_list(length=None)
    return sets

#Token Required Functions: via dependency on oauth2 password bearer through get_current_user function
@router.post("/set", response_model=Set)
async def create_set(newSet: Set = Body(...), user = Depends(get_current_user))->Set:
    newSet.username = user["username"]
    newSet = jsonable_encoder(newSet)
    set = await set_coll.insert_one(newSet)
    createdSet = await set_coll.find_one({"_id": set.inserted_id})
    return createdSet

@router.delete("/set/{set_id}")
async def delete_set(id: int, user = Depends(get_current_user)):
    set = await set_coll.delete_one({"position": id})
    #set is of type pymongo.Results.DeleteResult, check pymongo doc for more info
    if set.deleted_count == 1:
        return {"msg": "Set successfully deleted!"}
    raise HTTPException(status_code=400, detail="This set could not be deleted. Please try again later")

@router.put("/set/{set_id}")
async def update_set(set : Set = Body(...), user = Depends(get_current_user)):
    updated_set = await set_coll.update_one({"position": set.position}, {"$set": set})
    #updated_set is of type pymongo.Results.UpdatedResult, check pymongo doc for more info on returned fields
    if updated_set.modified_count == 1: 
        return {"msg": "Set was successfully updated!"}
    raise HTTPException(status_code=400, detail="This set could not be updated. Please try again later")