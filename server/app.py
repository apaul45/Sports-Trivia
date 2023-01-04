from fastapi import FastAPI
import motor.motor_asyncio
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

load_dotenv()
db_key = os.getenv("DB_KEY")
database = motor.motor_asyncio.AsyncIOMotorClient(db_key).st

questions_coll = database.get_collection("questions")
set_coll = database.get_collection("sets")
users_coll = database.get_collection("users")

#Include the different endpoints for each collection
from db_routes import question, sets, users
from aggregation.routes import router as aggregation_router

app.include_router(users.router)
app.include_router(question.router)
app.include_router(sets.router)
app.include_router(aggregation_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return "Hello FastAPI!"
