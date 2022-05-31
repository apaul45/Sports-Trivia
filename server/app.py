from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import motor.motor_asyncio #Motor serves as a MongoDB driver: API that allows non blocking access to MongoDB

app = FastAPI() #Creates an instance of an api to use
database = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/').sports_trivia #Connecting to MongoDB..

origins = [
    "https://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"]
)
@app.get("/")
async def root():
    return {"message": "Hello World"}