from typing import List, Optional
from pydantic import BaseModel, Field
from bson.objectid import ObjectId
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter

#Can modularize path operations w/the API Router
router = APIRouter(
    prefix="/questions",
    tags=["questions"],
)

#Field(...) is used to indicate a required field
class Question(BaseModel):
    question: str = Field(...)
    answer: str = Field(...)
    username: str = Field(...)
    difficulty: str = Field(...)
    player: str = Field(...)
    tags: List[str] = []

import sys
sys.path.insert(0,"..")
from server.app import questions_coll

#Controller functions
@router.get("/{question_id}", response_model=Question)
async def get_question(id: str) -> Question:
    question = await questions_coll.find_one({"_id":ObjectId(id)})
    return question

@router.post("/", response_model=Question)
async def create_question(question: Question) -> Question:
    question = jsonable_encoder(question)
    newQuestion = await questions_coll.insert_one(question)
    createdQuestion = await questions_coll.find_one({"_id": newQuestion.inserted_id})
    return createdQuestion

@router.delete("/{question_id}", response_model=Question)
async def delete_question(id: str) -> Question:
    question = await questions_coll.delete_one({"_id" : ObjectId(id)})
    return question

@router.put("/{question_id}", response_model=Question)
async def update_question(question: Question) -> Question:
    question = jsonable_encoder(question)
    updated_question = await questions_coll.findOneAndUpdate({question._id},{question})
    return updated_question