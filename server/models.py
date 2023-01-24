from bson.objectid import ObjectId
import pydantic

from fastapi.security import OAuth2
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi import Request
from fastapi.security.utils import get_authorization_scheme_param
from fastapi import HTTPException
from fastapi import status
from typing import Optional
from typing import Dict

class PyObjectId(ObjectId):

    @classmethod
    def __get_validators__(cls):

        yield cls.validate

    @classmethod
    def validate(cls, v):

        if not ObjectId.is_valid(v):

            raise ValueError("Invalid objectid")

        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):

        field_schema.update(type="string")

# fix ObjectId & FastApi conflict
pydantic.json.ENCODERS_BY_TYPE[ObjectId]=str
pydantic.json.ENCODERS_BY_TYPE[PyObjectId]=str

class OAuth2PasswordBearerWithCookie(OAuth2):
    def __init__(
        self,
        tokenUrl: str,
        scheme_name: Optional[str] = None,
        scopes: Optional[Dict[str, str]] = None,
        auto_error: bool = True,
    ):
        if not scopes:
            scopes = {}
        flows = OAuthFlowsModel(password={"tokenUrl": tokenUrl, "scopes": scopes})
        super().__init__(flows=flows, scheme_name=scheme_name, auto_error=auto_error)

    async def __call__(self, request: Request) -> Optional[str]:
        authorization: str = request.cookies.get("access_token")  #changed to accept access token from httpOnly Cookie

        scheme, param = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None
        return param