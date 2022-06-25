from typing import List
from app import questions_coll, set_coll
from collections_db.users import get_current_user
from collections_db.sets import Set
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(tags=["aggregation"])

#Helper Functions

async def get_result(collection, stage_list):
    items = await collection.aggregate(stage_list).to_list(length=None)
    print(items)
    result = []
    for item in items: 
        if item["_id"] == None or item["_id"] == "missing" or type(item["_id"]) != "str":
            del item["_id"]
        result.append(item)
    return result

#Helper for getting questions associated with a player or user
async def get_player_user_questions(query_field: str, query_value: str):
    match_stage = {
        "$match": {
            query_field: query_value
        }
    }
    # #$$ROOT allows for keeping all the fields of a document
    # group_stage = {
    #     "$group": {
    #         "_id": "$difficulty",
    #         "doc": {
    #             "$first": "$$ROOT"
    #         }
    #     }
    # }
    # #Replace root will promote the document to the top
    # replace_root_stage = {
    #     "$replaceRoot": {
    #         "newRoot": "$doc"
    #     }
    # }
    return await get_result(questions_coll, [match_stage])

#Routes

#Aggregation Routes for Questions
@router.get("/questions/{player_name}", response_description="Gets all the questions associated with a specific player, grouped by difficulty")
async def get_player_questions(player: str, user = Depends(get_current_user)):
    return await get_player_user_questions("player", player)

@router.get("/questions/{username}", response_description="Gets the questions associated with a user, grouped by difficulty")
async def get_user_questions(username: str):
    return await get_player_questions("username", username)

@router.get("/tag-questions", response_model = List[Set], response_description="Gets all the questions associated with certain tags")
async def get_tag_questions(tags: List) -> List[Set]:
    tags = [] 
    tags = await set_coll.find({"tags": tags}, {'_id': 0}).to_list(length = None)
    return tags

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
                "$first": "$$ROOT"
            }
        }
    }
    replace_root_stage= {
        "$replaceRoot": {
            "newRoot": "doc"
        }
    }
    return await get_result(set_coll, [match_stage, group_stage, replace_root_stage])

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
    return await get_result(set_coll, [group_stage])

