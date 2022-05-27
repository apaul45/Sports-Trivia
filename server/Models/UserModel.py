#Pydantic allows auto creation of JSON schemas from models
from typing import List

from pydantic import BaseModel
from SetModel import QuestionSet

class User(BaseModel):
    username: str
    email: str
    passwordHash: str
    sets: List[QuestionSet] = []
