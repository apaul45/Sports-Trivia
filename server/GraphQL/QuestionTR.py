from typing import List
import strawberry
from app import database

questions_coll = database.questions

@strawberry.type
class Question:
    question: str
    answer: str 
    username: str
    difficulty: str
    player: str 
    tags: List[str] = []

@strawberry.type
class Query:
    @strawberry.field
    async def get_question(id: Number) -> Question:
        try:
            question = await questions_coll.find_one({"_id":id})
            return question
        except:
            return "Question not found"

@strawberry.type
class Mutation:
    @strawberry.field
    async def create_question(question: Question) -> Question:
        try:
            newQuestion = await questions_coll.insert_one(question)
            return newQuestion
        except:
            return None

    @strawberry.field 
    async def delete_question(id) -> Question:
        question = await questions_coll.delete_one({"_id" : id})
        return question

    @strawberry.field
    async def update_question(question: Question) -> str:
        try:
            updated_prediction = await questions_coll.findOneAndUpdate({question._id},{question})
            return updated_prediction
        except:
            return None




