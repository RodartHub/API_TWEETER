#Python
from uuid import UUID
from datetime import date
from typing import Optional

#Pydantic
from pydantic import BaseModel, EmailStr, Field

#Models
class UserBase(BaseModel):
    user_id : UUID = Field(...)
    email: EmailStr = Field(...)


class User(UserBase):
    
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None)
    
class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
        )

class LoginOut(BaseModel):
    email: EmailStr = Field(...)
    message: str = Field(default='Login successfully!')

class UserRegister(User, UserLogin):
    pass