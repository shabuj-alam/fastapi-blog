from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict

from database.users_schema import UserResponse

class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)

class PostCreate(PostBase):
    user_id: int

class PostUpdate(BaseModel):
    title: str = Field(default=None, min_length=1, max_length=100)
    content: str = Field(default=None, min_length=1)

class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    date_posted: datetime
    author: UserResponse
