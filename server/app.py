from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import motor.motor_asyncio #Motor serves as a MongoDB driver: API that allows non blocking access to MongoDB
from pydantic import BaseModel
from typing import List
app = FastAPI() #Creates an instance of an api to use
database = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/').st #Connecting to MongoDB..

#from QuestionTR import Question

users_coll = database.users
questions_coll = database["questions"]
set_coll = database.sets

class Question(BaseModel):
    question: str
    answer: str 
    username: str
    difficulty: str
    player: str 
    tags: List[str] = []


origins = [
    "https://localhost:8080"
]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins = origins,
#     allow_credentials = True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/questions/{question_id}")
async def get_question(id):
    try:
        question = await questions_coll.find_one({"_id":id})
        return question
    except:
        return "Question not found"

@app.post("/questions/", response_model= Question)
async def create_question(question: Question):
    try:
        newQuestion = await questions_coll.insert_one(question)
        return newQuestion
    except:
        return None

@app.delete("/questions/{question_id}", response_model = Question)
async def delete_question(id):
    question = await questions_coll.delete_one({"_id" : id})
    return question

@app.put("/questions/{question_id}", response_model=str)
async def update_question(question: Question):
    try:
        update_question = await questions_coll.findOneAndUpdate({question._id},{question})
        return "Question successfully updated"
    except:
        return "Question could not be updated"



