#Python
import json
from typing import List
from uuid import UUID

# FastAPI
from fastapi import APIRouter, status, Body, Form, Path, HTTPException

#Pydantic

from pydantic import EmailStr

#data

DATAUSER_PATH = 'data/users.json'

#Models

from models.users import User, UserRegister, LoginOut

router = APIRouter()

## Users----------------------------------------------------------

### Register a user
@router.post(
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
    with open(DATAUSER_PATH, 'r+', encoding='utf-8') as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict['user_id'] = str(user_dict['user_id'])
        user_dict['birth_date'] = str(user_dict['birth_date'])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user


### Login a user
@router.post(
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
    with open(DATAUSER_PATH, 'r+', encoding='utf-8') as f:
        data = json.loads(f.read())
        for user in data:
            if email == user['email'] and password == user['password']:
                return LoginOut(email=email)
        return LoginOut(email=email, message='Login Unsuccessfully')


###Show all users
@router.get(
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
@router.get(
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
@router.delete(
    path='/users/{user_id}/delete',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Delete a User',
    tags=['Users']
)
def delete_a_user():
    pass

###Update a user
@router.put(
    path='/users/{user_id}/update',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Update a user',
    tags=['Users']
)
def update_a_user():
    pass
