from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi.staticfiles import StaticFiles

from .auth.base_config import auth_backend, fastapi_users
from .auth.schemas import UserRead, UserCreate

from .operations.router import router as router_operation
from .tasks.router import router as router_tasks
from .pages.router import router as router_pages
from .chat.router import router as router_chat

from redis import asyncio as aioredis

app = FastAPI(title="Trading App")

app.mount("/static", StaticFiles(directory="src/static"), name="static")

origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],  # "GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"
    allow_headers=["*"]   # "Content-Type", "Set-Cookie", "Access-Control-Allow-Headers",
                          # "Access-Control-Allow-Origin", "Authorization"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    router_operation,
    prefix="/operations",
    tags=["Operation"]
)

app.include_router(
    router_tasks,
    prefix="/tasks",
    tags=["Router Tasks"]
)

app.include_router(
    router_pages,
    prefix="/pages",
    tags=["Pages"]
)

app.include_router(
    router_chat,
    prefix="/chat",
    tags=["Chat"]
)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
