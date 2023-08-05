from datetime import datetime
from typing import Optional

from fastapi_users import schemas
from fastapi_users.schemas import PYDANTIC_V2


class UserRead(schemas.BaseUser[int]):
    username: str
    role_id: int


class UserCreate(schemas.BaseUserCreate):
    username: str
    role_id: int
    register_at: datetime = datetime.utcnow()
