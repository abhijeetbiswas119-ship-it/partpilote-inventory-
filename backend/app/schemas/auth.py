

from pydantic import BaseModel, EmailStr


# ---------- Register ----------
class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str = "viewer"


# ---------- Login ----------
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# ---------- Response ----------
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"