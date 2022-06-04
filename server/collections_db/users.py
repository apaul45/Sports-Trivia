from typing import List
from pydantic import BaseModel, Field
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException, Depends
from fastapi_jwt_auth import AuthJWT
from collections_db.sets import Set
from passlib.context import CryptContext

#Can modularize path operations w/the API Router
router = APIRouter(
    prefix = "/users",
    tags= ["users"]
)

#Field(...) is used to indicate a required field
class User(BaseModel):
    username: str = Field(...)
    email: str = Field(...)
    passwordHash: str = Field(...)
    sets: List[Set]

class LoggedInUser(BaseModel):
    username: str = Field(...)
    password: str = Field(...)

import sys
sys.path.insert(0,"..")
from server.app import users_coll

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register")
async def register_user(user:User, auth: AuthJWT = Depends()):
    username = user.username
    email = user.email
    existing_username = await users_coll.find_one({"username": username})
    existing_email = await users_coll.find_one({"email":email})
    if existing_username:
        raise HTTPException(status_code=400, detail="A user with this username already exists.")
    elif existing_email: 
        raise HTTPException(status_code=400, detail="A user with this email already exists")
    else:
        user.passwordHash = pwd_context.hash(user.passwordHash)
        user = jsonable_encoder(user)
        new_user = await users_coll.insert_one(user)
        created_user = await users_coll.find_one({"_id":new_user.inserted_id},{'_id': 0})
        #Create and store a JWT for the new user
        token = auth.create_access_token(subject=created_user.username)
        auth.set_access_cookies(token)
        return created_user

@router.get("/login")
async def login_user(user:LoggedInUser, auth: AuthJWT = Depends()):
    existing_user = await users_coll.find_one({"username": user.username})
    if not existing_user:
        raise HTTPException(status_code=400, detail="Incorrect username")
    elif not pwd_context.verify(user.password, existing_user.passwordHash):
        raise HTTPException(status_code=400, detail="Incorrect password")
    else:
        #Create and store a JWT for the new user
        token = auth.create_access_token(subject=user.username)
        auth.set_access_cookies(token)
        return user.username

@router.put("/")
async def update_user_sets(user: User):
    user = jsonable_encoder(user)
    user = await users_coll.findOneAndUpdate({user.inserted_id}, {user})
    return user