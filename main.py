#Python
import json
from typing import List
from uuid import UUID

# FastAPI
from fastapi import FastAPI, status, Body, Form, Path, HTTPException

#Pydantic

from pydantic import EmailStr

#Models

from models import User, UserBase, UserLogin, UserRegister, LoginOut
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
def signup(
    user: UserRegister = Body(...)
):
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
    - **birth_day: datetime**
    '''
    with open('users.json', 'r+', encoding='utf-8') as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict['user_id'] = str(user_dict['user_id'])
        user_dict['birth_date'] = str(user_dict['birth_date'])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user



### Login a user
@app.post(
    path='/login',
    response_model=LoginOut,
    status_code=status.HTTP_200_OK,
    summary='Login a User',
    tags=['Users']
)
def login(
    email: EmailStr = Form(...),
    password: str = Form(...)
):
    '''
    Login 

    This path operation login a person in the app

    Parameters:
    - Request body parameters:
        - email: EmailStr
        - password: str

    Returns a LoginOut model with username and message
    '''
    with open('users.json', 'r+', encoding='utf-8') as f:
        data = json.loads(f.read())
        for user in data:
            if email == user['email'] and password == user['password']:
                return LoginOut(email=email)
        return LoginOut(email=email, message='Login Unsuccessfully')


###Show all users
@app.get(
    path='/users',
    response_model= List[User],
    status_code=status.HTTP_200_OK,
    summary='Show all users',
    tags=['Users']
)
def show_all_users():
    '''
    This path operation shows all users in the app

    Parameters:
    -

    Returns a json list with all users in the app, with the 
    following keys:
    - **user_id: UUID**
    - **email: EmailStr**
    - **first_name: str**
    - **last_name: str**
    - **birth_day: datetime**

    '''

    with open('users.json', 'r', encoding='utf-8') as f:
        results = json.loads(f.read())
        return results

###Show a user
@app.get(
    path='/users/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Show a User',
    tags=['Users']
)
def show_a_user(
    user_id: UUID = Path(
        ...,
        title='User ID',
        description='This is the user ID',
        example='3fa85f64-5717-4562-b3fc-2c963f66afa6'
    )
    ):
    '''
    Show a User

    This path operation show if a person exist in the app

    Parameters:
    - **user_id: UUID**

    Returns a json with user data:
    - **user_id: UUID**
    - **email: EmailStr**
    - **first_name: str**
    - **last_name: str**
    - **birth_day: datetime**
    '''
    with open('users.json', 'r', encoding='utf-8') as f:
        results = json.loads(f.read())
        id = str(user_id)
        for data in results:
            if data['user_id'] == id:
                return data
            else:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"This {user_id} does'nt exist!"
                )

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
    '''
    This path operation shows all tweets in the app

    Parameters:
    -

    Returns a json list with all tweets in the app, with the 
    following keys:
    - **tweet_id: UUID** 
    - **content: str**
    - **create_at: datetime**
    - **updated_at: Optional[datetime]**
    - **by: User**

    '''

    with open('tweets.json', 'r', encoding='utf-8') as f:
        results = json.loads(f.read())
        return results
    

#Post a tweey
@app.post(
    path='/post',
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary='Post a tweet',
    tags=['Tweets']
)
def post(tweet: Tweet = Body(...)):
    '''
    Post a tweet

    This path operation post a tweet in the app.

    Parameters:
    - Request body parameter
        - **tweet: Tweet**

    Returns a json with the basic tweet information:
    - **tweet_id: UUID** 
    - **content: str**
    - **create_at: datetime**
    - **updated_at: Optional[datetime]**
    - **by: User**

    '''
    with open('tweets.json', 'r+', encoding='utf-8') as f:
        results = json.loads(f.read())
        tweet_dict = tweet.dict()
        tweet_dict['tweet_id'] = str(tweet_dict['tweet_id'])
        tweet_dict['created_at'] = str(tweet_dict['created_at'])
        tweet_dict['updated_at'] = str(tweet_dict['updated_at'])
        tweet_dict['by']['user_id'] = str(tweet_dict['by']['user_id'])
        tweet_dict['by']['birth_date'] = str(tweet_dict['by']['birth_date'])

        results.append(tweet_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return tweet


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

