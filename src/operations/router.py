from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from .models import operation
from .schemas import OperationCreate
from ..database import get_async_session

from asyncio import sleep

router = APIRouter()


@router.get("/some_long_operation")
@cache(expire=45)
async def get_long_op():
    await sleep(4)
    return "Many many data"



@router.get("/")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.c.type == operation_type)
    result = await session.execute(query)
    return result.all()


@router.post("/")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
