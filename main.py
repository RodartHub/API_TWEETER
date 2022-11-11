#Python
from typing import List

# FastAPI
from fastapi import FastAPI, status

#Models

from models import User, UserBase, UserLogin
from models import Tweet

app = FastAPI()

#Path Operations

@app.get(
    path='/'
)
def home():
    return {'Twitter API':'Working!'}

## Users----------------------------------------------------------

@app.post(
    path='/signup',
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary='Register a User',
    tags=['Users']
)
def signup():
    pass

@app.post(
    path='/login',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Login a User',
    tags=['Users']
)
def login():
    pass

@app.get(
    path='/users',
    response_model= List[User],
    status_code=status.HTTP_200_OK,
    summary='Show all users',
    tags=['Users']
)
def show_all_users():
    pass

@app.get(
    path='/users/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Show a User',
    tags=['Users']
)
def show_a_user():
    pass

@app.delete(
    path='/users/{user_id}/delete',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Delete a User',
    tags=['Users']
)
def delete_a_user():
    pass

@app.put(
    path='/users/{user_id}/update',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Update a user',
    tags=['Users']
)
def update_a_user():
    pass


## Tweets



