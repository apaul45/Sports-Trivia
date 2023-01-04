#This file contains all the CRUD operations for a Question
from typing import List, Optional
from pydantic import BaseModel, Field
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends, Body, HTTPException

import sys
sys.path.insert(0,"..")
from server.id_model import PyObjectId

#Can modularize path operations w/the API Router
router = APIRouter(tags=["questions"])

#Field(...) is used to indicate a required field
class Question(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    question: str = Field(...)
    answer: str = Field(...)
    difficulty: str = Field(...)
    username: Optional[str]
    player: str = Field(...)
    tags: List[str] = []

    class Config:
        fields = {'id': '_id'}

class UpdateQuestionModel(BaseModel):
    question: Optional[str]
    answer: Optional[str]
    difficulty: Optional[str]
    username: Optional[str]
    player: Optional[str]
    tags: Optional[List[str]]

from server.app import questions_coll
from db_routes.users import get_current_user

@router.get("/questions")
async def get_all_questions():
    #Use {_id: 0} to ignore the _id field when requesting: this is to prevent issues regarding ObjectIds in MongoDB
    questions = await questions_coll.find({}).to_list(length=None)
    return questions

#Token Required Functions: via dependency on oauth2 password bearer through get_current_user function
@router.post("/question", response_model=Question)
async def create_question(question: Question = Body(...), user = Depends(get_current_user)) -> Question:
    #First verify that this question doesn't already exist 
    in_db = await questions_coll.find_one({"question": question.question})
    
    if in_db: 
        raise HTTPException(status_code= 400, detail = "This question already exists!")

    question.username = user["username"]
    question = jsonable_encoder(question)
    
    newQuestion = await questions_coll.insert_one(question)
    createdQuestion = await questions_coll.find_one({"_id": newQuestion.inserted_id})
    return createdQuestion

@router.delete("/question/{question}")
async def delete_question(question: str, user = Depends(get_current_user)):
    question = await questions_coll.delete_one({"question": question})
    #question is of type pymongo.Results.DeleteResult, check pymongo doc for more detail
    if question.deleted_count < 1:
        raise HTTPException(status_code=400, detail="This question could not be deleted. Please try again later")

    return {"msg": "Question successfully deleted!"}

@router.put("/question/{question}")
async def update_question(
    question: str, 
    question_obj: UpdateQuestionModel = Body(...), 
    user = Depends(get_current_user)
):
    question_obj = {k: v for k, v in question_obj.dict().items() if v is not None} #Needed to remove missing fields

    if len(question_obj) > 0: 
        updated_question = await questions_coll.update_one({"question": question}, {"$set": question_obj})
        #updated_question is of type pymongo.Results.UpdatedResult, check pymongo doc for more info on returned fields
        if updated_question.modified_count < 1:
            raise HTTPException(status_code=400, detail="Question could not be updated. Please try again later.")

    return {"msg": "Question successfully updated!"}