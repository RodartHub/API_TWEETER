#Python
from typing import List

# FastAPI
from fastapi import FastAPI, status

#Models

from models import User, UserBase, UserLogin
from models import Tweet

app = FastAPI()

#Path Operations

## Users----------------------------------------------------------

### Register a user
@app.post(
    path='/signup',
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary='Register a User',
    tags=['Users']
)
def signup():
    '''
    Signup

    This path operation registers a user in the app.

    Parameters:
        - Request body parameter
            - **user: UserRegister**

    Returns a json with the basic user information:
        - **user_id: UUID**
        - **email: EmailStr**
        - **first_name: str**
        - **last_name: str**
        - **birth_day: date**
    '''

### Login a user
@app.post(
    path='/login',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Login a User',
    tags=['Users']
)
def login():
    pass

###Show all users
@app.get(
    path='/users',
    response_model= List[User],
    status_code=status.HTTP_200_OK,
    summary='Show all users',
    tags=['Users']
)
def show_all_users():
    pass

###Show a user
@app.get(
    path='/users/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Show a User',
    tags=['Users']
)
def show_a_user():
    pass

###Delete a user
@app.delete(
    path='/users/{user_id}/delete',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Delete a User',
    tags=['Users']
)
def delete_a_user():
    pass

###Update a user
@app.put(
    path='/users/{user_id}/update',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Update a user',
    tags=['Users']
)
def update_a_user():
    pass


## Tweets-------------------------------------------

###Show all tweets
@app.get(
    path='/',
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary='Show all tweets',
    tags=['Tweets']
)
def home():
    return {'Twitter API':'Working!'}

#Post a tweey
@app.post(
    path='/post',
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary='Post a tweet',
    tags=['Tweets']
)
def post():
    pass

#Show a tweet
@app.get(
    path='/tweets/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Show a tweet',
    tags=['Tweets']
)
def show_a_tweet():
    pass

###Delete a tweet
@app.delete(
    path='/tweets/{tweet_id}/delete',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Delete a tweet',
    tags=['Tweets']
)
def delete_a_tweet():
    pass

###Update a tweet
@app.put(
    path='/tweets/{tweet_id}/update',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Update a tweet',
    tags=['Tweets']
)
def update_a_tweet():
    pass

