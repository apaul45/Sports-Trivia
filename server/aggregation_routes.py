from typing import List
from app import questions_coll, set_coll
from collections_db.question import Question
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

#This helper is used for the functions that retain all fields in group stage: like get_result but specific to these group of routes
async def get_result_docfields(collection, stage_list):
    items = await collection.aggregate(stage_list).to_list(length = None)
    print(items)
    result = []
    #Result of the aggregation is a list of objects, where each object contains the group id, and documents in the doc (in a field called "doc")
    for item in items:
        for document in item['doc']:
            del document["_id"]
        result.append(item)
    return result

#Helper for getting questions associated with a player or user
async def get_player_user_questions(query_field: str, query_value: str):
    match_stage = {
        "$match": {
            query_field: query_value
        }
    }
    #$$ROOT allows for keeping all the fields of a document- Must use $push on it to apply to all documents in a group
    group_stage = {
        "$group": {
            "_id": "$difficulty",
            "doc": {
                "$push": "$$ROOT"
            }
        }
    }
    return await get_result_docfields(questions_coll, [match_stage, group_stage])

#Routes

#Aggregation Routes for Questions
@router.get("/player-questions/{player}", response_description="Gets all the questions associated with a specific player, grouped by difficulty")
async def get_player_questions(player: str):
    return await get_player_user_questions("player", player)

@router.get("/user-questions/{user}", response_description="Gets the questions associated with a user, grouped by difficulty")
async def get_user_questions(username: str):
    return await get_player_user_questions("username", username)

@router.post("/tag-questions", response_model = List[Question], response_description="Gets all the questions associated with certain tags")
async def get_tag_questions(tags: List) -> List[Question]:
    #Use $all operator to allow for checking if one or both tags exist in a question's tag array, and filter by that
    query = {
        "tags": {
            "$all": tags
        }
    }
    return await questions_coll.find(query, {'_id': 0}).to_list(length = None)

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
    return await get_result_docfields(set_coll, [match_stage, group_stage])

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

