from typing import List

import strawberry
from app import database
from SetTR import QuestionSet

users_coll = database.users

@strawberry.type
class User:
    username: str
    email: str
    passwordHash: str
    sets: List[QuestionSet] = []

