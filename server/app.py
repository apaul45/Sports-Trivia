from fastapi import FastAPI
import motor.motor_asyncio
app = FastAPI()
database = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017").st

#Question Routes
from collections_db.question import Question
import collections_db.question

@app.get("/")
def root():
    return {"Hello":"FastAPI!"}

@app.get("/questions/{question_id", response_model=Question)
async def GET_QUESTION(id):
    question = await collections_db.question.get_question(id)
    return question

@app.post("/questions/", response_model=Question)
async def post_question(question: Question):
    question = await collections_db.question.create_question(question)
    return question

@app.delete("/questions/{question_id}", response_model=Question)
async def DELETE_QUESTION(id):
    question = await collections_db.question.delete_question(id)
    return question

@app.put("/questions/{question_id}", response_model=Question)
async def put_question(id):
    question = await collections_db.question.update_question(id)
    return question

#Set Routes
from collections_db.sets import Set
import collections_db.sets

@app.get("/sets/{set_id}", response_model=Set)
async def GET_SET(id):
    set = await collections_db.sets.get_set(id)
    return set

@app.post("/sets/", response_model=Set)
async def post_set(set: Set):
    set = await collections_db.sets.create_set(set)
    return set

@app.delete("/sets/{set_id}", response_model=Set)
async def remove_set(id):
    set = await collections_db.sets.delete_set(id)
    return set

@app.put("/sets/{set_id}", response_model=Set)
async def put_set(id):
    set = await collections_db.sets.update_set(id)
    return set