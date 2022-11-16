#Python
import json
from typing import List
from uuid import UUID

# FastAPI
from fastapi import APIRouter, status, Body, Form, Path, HTTPException

#Models

from models.tweets import Tweet

#data

DATAUSER_PATH = 'data/tweets.json'

#tools

from models.tools import read_data


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

    with open(DATAUSER_PATH, 'r', encoding='utf-8') as f:
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
    with open(DATAUSER_PATH, 'r+', encoding='utf-8') as f:
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
def show_a_tweet(
    tweet_id: UUID = Path(
        ...,
        title= 'tweet_id',
        description='This is the tweet ID'
    )
):
    '''
    Show a tweet

    This is path operation show a tweet

    Parameters:
    - **tweet_id: UUID**

    Returns a json with tweet data:
    - **tweet_id: UUID** 
    - **content: str**
    - **create_at: datetime**
    - **updated_at: Optional[datetime]**
    - **by: User**
    '''
    results = read_data(DATAUSER_PATH)
    id = str(tweet_id)    
    for data in results:    
        if data['tweet_id'] == id:
            return data     
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"This {tweet_id} does'nt exist!"
        )

###Delete a tweet
@router.delete(
    path='/tweets/{tweet_id}/delete',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Delete a tweet',
    tags=['Tweets']
)
def delete_a_tweet(
    tweet_id: UUID = Path(
        ...,
        title='User ID',
        description= 'This is the user ID'
    )
):
    '''
    Delete a Tweet

    This path operation delete a tweet in the app

    Parameter:
    - **tweet_id: UUID**

    Returns a json with deleted user data:
    - **tweet_id: UUID**
    - **content: str**
    - **created_at: datetime**
    - **updated_at: datetime**
    - **by: User** -->
        - **email: EmailStr**
        - **first_name: str**
        - **last_name: str**
        - **birth_day: datetime**
    '''

    with open(DATAUSER_PATH, 'r+', encoding='utf-8') as f:
        results = json.loads(f.read())
        id = str(tweet_id)

        for data in results:
            if data['tweet_id'] == id:
                results.remove(data)
                with open(DATAUSER_PATH, 'w', encoding='utf-8') as f:
                    f.seek(0)
                    f.write(json.dumps(results))
                return data
            else:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"This {tweet_id} doesn't exist! "
                )

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

