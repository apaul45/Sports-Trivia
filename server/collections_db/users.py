from typing import List
from pydantic import BaseModel, Field
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException, Depends, Response
from fastapi_jwt_auth import AuthJWT
from collections_db.sets import Set
from passlib.context import CryptContext
from auth.token import Settings, get_config

#Can modularize path operations w/the API Router
router = APIRouter(
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
async def register_user(user:User, response: Response, auth: AuthJWT = Depends()):
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
        token = auth.create_access_token(subject=created_user["username"])
        #In order to send the cookie in the response, a parameter of 
        #type Response can be included in the path function, and then passed
        #into set_access_cookies. When this function returns an object now, the cookie 
        #will be included along with that object
        auth.set_access_cookies(token, response=response)
        return {"msg": "User successfully registered"}

@router.get("/login")
async def login_user(user:LoggedInUser, response: Response, auth: AuthJWT = Depends()):
    existing_user = await users_coll.find_one({"username": user.username})
    if not existing_user:
        raise HTTPException(status_code=400, detail="Incorrect username")
    elif not pwd_context.verify(user.password, existing_user.passwordHash):
        raise HTTPException(status_code=400, detail="Incorrect password")
    else:
        #Create, store, and return a JWT in a cookie
        token = auth.create_access_token(subject=user.username)
        auth.set_access_cookies(token, response=response)
        return {"msg": "User successfully logged in"}

@router.put("/usersets")
async def update_user_sets(user: User):
    user = jsonable_encoder(user)
    user = await users_coll.findOneAndUpdate({user.inserted_id}, {user})
    return user

@router.put("/logout")
async def logout(auth: AuthJWT = Depends()):
    auth.jwt_required()
    auth.unset_jwt_cookies()
    return {"msg": "Successfully logged out"}