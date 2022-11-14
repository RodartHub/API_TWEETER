#Python
from uuid import UUID
from datetime import datetime
from typing import Optional

#Pydantic
from pydantic import BaseModel, Field

#Users
from models.users import User

#Models

class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)

