#FastAPI 

from fastapi import FastAPI

#Local packages

from paths import user, tweets

app = FastAPI()

#Includes the paths from paths folder

app.include_router(user.router)
app.include_router(tweets.router)

