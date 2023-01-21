#This file contains all the CRUD operations for a Question
from typing import List, Optional
from pydantic import BaseModel, Field
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends, Body, HTTPException

import sys
sys.path.insert(0,"..")
from server.id_model import PyObjectId

# import requests 
# from bs4 import BeautifulSoup
# import random

#Can modularize path operations w/the API Router
router = APIRouter(tags=["questions"])

#Field(...) is used to indicate a required field
class Question(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    question: str = Field(...)
    answer: str = Field(...)
    difficulty: str = Field(...)
    username: str = Field(...)
    player: Optional[str]
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

# @router.post("/scrape-questions")
# async def scrape_questions():
#     #Scraped from triviawell.com
#     base_link = "https://www.triviawell.com/questions/sports/"

#     content = requests.get(base_link).content
#     scraper = BeautifulSoup(content, "html.parser")

#     total_pages = len(scraper.find_all("li", class_="page-item d-none d-md-inline"))

#     for i in range(total_pages):
#         print("------------------PAGE " + str(i+1) + "------------------")

#         difficulty = ["easy", "medium", "hard"]

#         link = base_link + str(i+1)

#         content = requests.get(link).content
#         scraper = BeautifulSoup(content, "html.parser")

#         page_questions = scraper.find_all("div", class_="card-body")

#         for question in page_questions:
#             q = question.find("h4").a.text
#             answer = question.find("ul", class_="d-none answer").li.text
#             tags = question.find("ul", class_="mb-3 list-inline").li.find_all("a")

#             tags = [a.text for a in tags]
#             tags.remove("Sports")

#             question = Question(
#                 question=q.strip(), 
#                 answer=answer.strip(), 
#                 tags=tags,
#                 username="Triviawell",
#                 difficulty=random.choice(difficulty)
#             )

#             await questions_coll.insert_one(jsonable_encoder(question))
    
#     query = [
#         {
#             '$group': {
#                 '_id': '$question',
#                 'doc': {
#                     '$first': '$$ROOT'
#                 }
#             }
#         }, {
#             '$replaceRoot': {
#                 'newRoot': '$doc'
#             }
#         }, {
#             '$out': 'questions'
#         }
#     ]

#     questions_coll.aggregate(query)

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