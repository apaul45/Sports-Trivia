#Pydantic allows auto creation of JSON schemas from models
from typing import List

from pydantic import BaseModel

class Question(BaseModel):
    question: str
    answer: str
    username: str
    difficulty: str
    player: str
    tags: List[str] = []