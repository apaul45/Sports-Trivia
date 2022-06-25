from fastapi import FastAPI
import motor.motor_asyncio
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
database = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017").st
questions_coll = database.get_collection("questions")
set_coll = database.get_collection("sets")
users_coll = database.get_collection("users")

#Include the different endpoints for each collection
from collections_db import question, sets, users
from aggregation_routes import router as aggregation_router

app.include_router(users.router)
app.include_router(question.router)
app.include_router(sets.router)
app.include_router(aggregation_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:8080",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"Hello":"FastAPI!"}
