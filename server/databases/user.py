from typing import List
from app import database
from set import QuestionSet

users_coll = database.users

class User:
    username: str
    email: str
    passwordHash: str
    sets: List[QuestionSet] = []

