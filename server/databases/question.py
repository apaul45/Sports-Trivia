from typing import List, Number
from pydantic import BaseModel
from app import database

questions_coll = database.questions

class Question(BaseModel):
    question: str
    answer: str 
    username: str
    difficulty: str
    player: str 
    tags: List[str] = []


async def get_question(id: Number) -> Question:
    try:
        question = await questions_coll.find_one({"_id":id})
        return question
    except:
        return "Question not found"

async def create_question(question: Question) -> Question:
    try:
        newQuestion = await questions_coll.insert_one(question)
        return newQuestion
    except:
        return None
    
async def delete_question(id) -> Question:
    question = await questions_coll.delete_one({"_id" : id})
    return question

async def update_question(question: Question) -> str:
    try:
        updated_question = await questions_coll.findOneAndUpdate({question._id},{question})
        return updated_question
    except:
        return None




