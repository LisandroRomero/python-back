import email
from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    email:EmailStr
    password:str


class TokenResponse(BaseModel):
    access_token:str
    refresh_token:str
    token_type:str = "Bearer"


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    full_name: str

