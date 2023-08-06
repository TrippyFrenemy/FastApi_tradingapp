from datetime import datetime

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    username: str
    role_id: int


class UserCreate(schemas.BaseUserCreate):
    username: str
    role_id: int
    register_at: datetime = datetime.utcnow()
