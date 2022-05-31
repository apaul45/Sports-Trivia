import strawberry
from app import database
from typing import List
from QuestionTR import Question

set_coll = database.sets

@strawberry.type
class QuestionSet:
    username: str
    set: List[Question] = []

@strawberry.type
class Query:
    @strawberry.field
    async def get_set(id) -> QuestionSet:
        try:
            set = await set_coll.find_one({"_id":id})
            return set
        except:
            return None

@strawberry.type
class Mutation:
    @strawberry.field
    async def create_set(newSet:QuestionSet) -> QuestionSet:
        try:
            set = await set_coll.insert_one(newSet)
            return set
        except:
            return "Could not create this set"
    
    @strawberry.field
    async def delete_set(id) -> QuestionSet:
        try:
            set = await set_coll.delete_one({"_id":id})
            return set
        except:
            return None
    @strawberry.field
    async def update_set(set):
        try:
            await set_coll.findOneAndUpdate({set._id}, {set})
        except:
            return "Could not update this set"


