#This is a basic authentication system using Oauth2 and JWTs
from fastapi import Depends, APIRouter, HTTPException
import sys
sys.path.insert(0,"..")
from server.app import users_coll
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import JWTError, jwt
import os
from dotenv import load_dotenv

router = APIRouter(tags=["users"])

#Using OAuth2 with Password flow and Bearer token (ie, header Authorization with "Bearer {token}")
#As the tokenUrl is login, the user will be sending their info to the path "/login" to authenticate themselves
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

#pwd_context for checking and hashing passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#Creating/encoding a JWT using the secret from .env file
load_dotenv()
secret_key = os.getenv('JWT_SECRET')
algorithm = "HS256"

class User(BaseModel):
    username: str
    passwordHash: str

class RegisterUser(BaseModel):
    username: str
    password: str
    password_confirmed: str

class Token(BaseModel):
    access_token: str

#A user can register, but they must login after to receive a token (PasswordBearer only supports one url)
@router.post("/register")
async def register_user(user: RegisterUser):
    #Check if a user with this username currently exists already
    username_user = await users_coll.find_one({"username": user.username})
    if username_user:
        raise HTTPException(status_code=400, detail="A user with this username already exists")
    else:
        user.password = pwd_context.hash(user.password)
        user = jsonable_encoder(user)
        del user["password_confirmed"]
        user = await users_coll.insert_one(user)
        if user:
            return {"msg": "user successfully registered!"}
        raise HTTPException(status_code=400, detail="An error occurred while trying to register this user")
    
#OAuth2PasswordRequestForm is a dependency that creates a form with the entered username and password
#Since this routes path is "/token", it will be called once the user enters their info into the request form
@router.post("/login", response_model=Token)
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await users_coll.find_one({"username": form_data.username})
    
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username")
    if not pwd_context.verify(form_data.password, user["password"]):
        raise HTTPException(status_code=400, detail="Incorrect password")

    #Create and send a JWT for the user to use for authorization
    token = jwt.encode({"user": user["username"]}, secret_key, algorithm= algorithm)
    return {"access_token": token}

@router.get("/users")
async def get_all_users():
    #Use {_id: 0} to ignore the _id field when requesting: this is to prevent issues regarding ObjectIds in MongoDB
    #Adding {username: 1} allows for only returning the username of each document 
    users = await users_coll.find({},{'username': 1, '_id': 0}).to_list(length=None)
    return users

#From FastAPI documentation: this will serve as authorization for all routes
#Once the user authenticates, oauth2_scheme will check for their token, which is why its a dependency
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    username = None
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        username = payload.get("user")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await users_coll.find_one({"username": username})
    if user is None:
        raise credentials_exception
    return user
