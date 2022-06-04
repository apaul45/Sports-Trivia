from typing import List
from pydantic import BaseModel, Field
from bson.objectid import ObjectId
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter

#Can modularize path operations w/the API Router
router = APIRouter(
    prefix="/sets",
    tags=["sets"],
)

from server.collections_db.question import Question

#Field(...) is used to indicate a required field
class Set(BaseModel):
    username: str = Field(...)
    set: List[Question]
    rating: int

import sys
sys.path.insert(0,"..")
from server.app import set_coll

@router.get("/{set_id}", response_model=Set)
async def get_set(id)->Set:
    set = await set_coll.find_one({"_id":ObjectId(id)})
    return set

@router.post("/", response_model=Set)
async def create_set(newSet:Set)->Set:
    newSet = jsonable_encoder(newSet)
    set = await set_coll.insert_one(newSet)
    createdSet = await set_coll.find_one({"_id": set.inserted_id})
    return createdSet

@router.delete("/{set_id}", response_model=Set)
async def delete_set(id)->Set:
    set = await set_coll.delete_one({"_id":ObjectId(id)})
    return set

@router.put("/{set_id}", response_model=Set)
async def update_set(set : Set)->Set:
    set = jsonable_encoder(set)
    set = await set_coll.findOneAndUpdate({set._id}, {set})
    return set