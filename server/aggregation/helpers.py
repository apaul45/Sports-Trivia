from app import questions_coll

#Helper for getting questions associated with a player or user
async def get_player_user_questions(query_obj):
    match_stage = {
        "$match": query_obj
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

    questions = await questions_coll.aggregate([match_stage, group_stage]).to_list(length = None)
    return questions