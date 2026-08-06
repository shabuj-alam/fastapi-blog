from typing import Annotated

from fastapi import (
    Depends, 
    APIRouter, 
    HTTPException, 
    status
)

from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from database import models
from database.database import ( 
    get_db
)
from database.posts_schema import (
    PostCreate, 
    PostResponse, 
    PostUpdate
)
