from pydantic import BaseModel, Field, ConfigDict, EmailStr

class UserBase(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    email: EmailStr = Field(min_length=1, max_length=100)
    

class UserCreate(UserBase):
    password: str = Field(min_length=6, max_length=100)

class UserPublic(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    image_file: str | None
    image_path: str 

class UserPrivate(UserPublic):
    model_config = ConfigDict(from_attributes=True)

    email: EmailStr

class UserUpdate(BaseModel):
    username: str = Field(default=None, min_length=1, max_length=50)
    email: EmailStr = Field(default=None, min_length=1, max_length=100)

class Token(BaseModel):
    access_token: str
    token_type: str
