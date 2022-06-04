#This file is used to set up the creation and sending of JWTs in cookies
from pydantic import BaseModel
from fastapi_jwt_auth import AuthJWT
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseModel):
    authjwt_secret_key: str = os.getenv('JWT_SECRET')
     # Configure application to store and get JWT from cookies
    authjwt_token_location: set = {"cookies"}
    # Only allow JWT cookies to be sent over https
    authjwt_cookie_secure: bool = False
    # Enable csrf double submit protection. default is True
    authjwt_cookie_csrf_protect: bool = True
    # Change to 'lax' in production to make your website more secure from CSRF Attacks, default is None
    # authjwt_cookie_samesite: str = 'lax'

@AuthJWT.load_config
def get_config():
    return Settings()

