from fastapi import FastAPI
import motor.motor_asyncio

app = FastAPI()
database = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017").st
questions_coll = database.get_collection("questions")
set_coll = database.get_collection("sets")
users_coll = database.get_collection("users")

#Include the different endpoints for each collection
from collections_db import question, sets, users

app.include_router(users.router)
app.include_router(question.router)
app.include_router(sets.router)

@app.get("/")
def root():
    return {"Hello":"FastAPI!"}
