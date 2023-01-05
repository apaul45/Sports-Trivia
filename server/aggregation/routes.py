from typing import List
from fastapi import APIRouter
from app import questions_coll, set_coll
from db_routes.question import Question
from aggregation.helpers import get_player_user_questions

router = APIRouter(tags=["aggregation"])

#Aggregation route for all filters in front end
@router.post("/filter-questions", response_description="Filters by search text, tags, and/or users. Accepts mongodb expressions only.")
async def get_filtered_questions(filters: List[object]):
    questions = questions_coll.find({"$and": filters})
    return await questions.to_list(length = None)

#Aggregation Routes for Questions
@router.get("/player-questions/{player}", response_description="Gets all the questions associated with a specific player, grouped by difficulty")
async def get_player_questions(player: str):
    return await get_player_user_questions({"player": player})

@router.get("/user-questions/{user}", response_description="Gets the questions associated with a user, grouped by difficulty")
async def get_user_questions(username: str):
    return await get_player_user_questions({"username": username})

@router.post("/tag-questions", response_description="Gets all the questions associated with certain tags")
async def get_tag_questions(tags: List) -> List[Question]:
    query = {
        "tags": {
            "$all": tags
        }
    }
    
    questions = questions_coll.find(query)
    return await questions.to_list(length=None)

@router.get("/tags", response_model=List[str], response_description="Returns a list of all unique tags found linked to questions")
async def get_tags() -> List[str]:
    return await questions_coll.distinct("tags")

#Aggregation Routes for Sets
@router.get("/sets/{username}", response_description="Returns the sets made by a user, along with their average rating")
async def get_user_sets(username: str):
    match_stage = {
        "$match": {
            "username": username
        }
    }
    group_stage = {
        "$group": {
            "_id": None,
            "averageRating": {
                "$avg": "$rating"
            },
            "doc": {
                "$push": "$$ROOT"
            }
        }
    }

    sets = await set_coll.aggregate([match_stage]).to_list(length=None)
    return sets

@router.get("/users-ratings", response_description="Returns a list of users containing their average set rating")
async def get_users_ratings():
    group_stage = {
        "$group": {
            "_id": "$username",
            "averageRating": {
                "$avg": "$rating"
            },
            "count": {
                "$sum": 1
            },
        }
    }

    sets = await set_coll.aggregate([group_stage]).to_list(length=None)
    return sets

