#Python
from uuid import UUID
from datetime import date, datetime
from typing import Optional

#Pydantic
from pydantic import BaseModel, EmailStr, Field

# FastAPI
from fastapi import FastAPI

#Models

from models import User, UserBase, UserLogin
from models import Tweet

app = FastAPI()

@app.get(
    path='/'
)
def home():
    return {'Twitter API':'Working!'}