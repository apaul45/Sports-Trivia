from typing import List, Optional
from pydantic import BaseModel, Field, PyObject
from bson.objectid import ObjectId
from fastapi.encoders import jsonable_encoder

#Field(...) is used to indicate a required field

class Question(BaseModel):
    id: Optional[str]
    question: str = Field(...)
    answer: str = Field(...)
    username: str = Field(...)
    difficulty: str = Field(...)
    player: str = Field(...)
    tags: List[str] = []

#Make sure to import the database variable from app AFTER defining the model
import sys
sys.path.insert(0,"..")
from server.app import database
questions_coll = database.get_collection("questions")

#Used to return the data as objects
def question_helper(question: Question) -> dict:
    return {
        "id": question["_id"],
        "question": question["question"],
        "answer": question["answer"],
        "username": question["username"],
        "difficulty": question["difficulty"],
        "player": question["player"],
        "tags": question["tags"]
    }

#Controller functions

async def get_question(id: str) -> Question:
    question = await questions_coll.find_one({"_id":ObjectId(id)})
    return question

async def create_question(question: Question) -> Question:
    question = jsonable_encoder(question)
    newQuestion = await questions_coll.insert_one(question)
    createdQuestion = await questions_coll.find_one({"_id": newQuestion.inserted_id})
    return createdQuestion
    
async def delete_question(id: str) -> Question:
    question = await questions_coll.delete_one({"_id" : ObjectId(id)})
    return question

async def update_question(question: Question) -> Question:
    question = jsonable_encoder(question)
    updated_question = await questions_coll.findOneAndUpdate({question._id},{question})
    return updated_question