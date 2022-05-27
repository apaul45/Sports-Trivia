#Pydantic allows auto creation of JSON schemas from models
from typing import List

from pydantic import BaseModel
from QuestionModel import Question

class QuestionSet(BaseModel):
    set: List[Question] = []
    username: str