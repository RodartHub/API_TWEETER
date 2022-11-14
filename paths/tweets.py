#Python
import json
from typing import List
from uuid import UUID

# FastAPI
from fastapi import FastAPI, APIRouter, status, Body, Form, Path, HTTPException

#Models

from models.users import User, UserBase, UserLogin, UserRegister, LoginOut
from models.tweets import Tweet

router = APIRouter()

## Tweets-------------------------------------------

###Show all tweets
@router.get(
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
    

#Post a tweet
@router.post(
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
@router.get(
    path='/tweets/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Show a tweet',
    tags=['Tweets']
)
def show_a_tweet():
    pass

###Delete a tweet
@router.delete(
    path='/tweets/{tweet_id}/delete',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Delete a tweet',
    tags=['Tweets']
)
def delete_a_tweet():
    pass

###Update a tweet
@router.put(
    path='/tweets/{tweet_id}/update',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Update a tweet',
    tags=['Tweets']
)
def update_a_tweet():
    pass

