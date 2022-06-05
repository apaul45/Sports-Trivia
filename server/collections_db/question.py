from typing import List
from pydantic import BaseModel, Field
from bson.objectid import ObjectId
from fastapi.encoders import jsonable_encoder
from fastapi_jwt_auth import AuthJWT
from fastapi import APIRouter, Depends
from auth.token import Settings, get_config

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
from auth.token import Settings, get_config

@router.get("/{question_id}")
async def get_question(id: str):
    question = None
    if id == "get_all":
        question = await questions_coll.find({})
    else:
        question = await questions_coll.find_one({"_id":ObjectId(id)})
    return question

#Token Required Functions
#When a request arrives, FastAPI will call the function specified by Depends(),
#and include the result in the path operation's parameters
@router.post("/", response_model=Question)
async def create_question(question: Question, auth: AuthJWT = Depends()) -> Question:
    auth.jwt_required()
    question = jsonable_encoder(question)
    newQuestion = await questions_coll.insert_one(question)
    createdQuestion = await questions_coll.find_one({"_id": newQuestion.inserted_id})
    return createdQuestion

@router.delete("/{question_id}", response_model=Question)
async def delete_question(id: str, auth: AuthJWT = Depends()) -> Question:
    auth.jwt_required()
    question = await questions_coll.delete_one({"_id" : ObjectId(id)})
    return question

@router.put("/{question_id}", response_model=Question)
async def update_question(question: Question, auth: AuthJWT = Depends()) -> Question:
    auth.jwt_required()
    question = jsonable_encoder(question)
    updated_question = await questions_coll.findOneAndUpdate({question._id},{question})
    return updated_question