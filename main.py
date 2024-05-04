import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_framework import redis_dependency
from starlette.responses import FileResponse
from colorama import Fore
from api_description import description
from app.routers.AuthenticationRouter import AuthenticationRouter
from app.routers.TicketRouter import TicketRouter
from app.routers.UserRouter import UserRouter

app = FastAPI(
    title="ZooHub API",
    description=description,
    version="0.1.0",
    root_path="/api"
)

# noinspection PyTypeChecker
app.add_middleware(
    CORSMiddleware,
    # allow_origins=["http://localhost:3000"],
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(AuthenticationRouter)
app.include_router(UserRouter)
app.include_router(TicketRouter)


# noinspection PyTypeHints
@app.on_event("startup")
async def startup():
    try:
        await redis_dependency.init()
        print(f"{Fore.RED}CACHE:    Redis connection established{Fore.RESET}")
    except Exception as e:
        print(f"Redis connection initialization error: {e}")


@app.on_event("shutdown")
async def shutdown():
    try:
        # No Redis client closing for fastapi-framework.redis/redis_dependency
        # Just an improvisation here
        redis_dependency.redis.get("").close()
        print(f"{Fore.RED}CACHE:    Redis connection ended{Fore.RESET}")
    except Exception as e:
        print(f"Redis connection closing error: {e}")


# Route for FastApiDocs to display local images. Not to be exposed
@app.get(
    path="/img/{filename}",
    deprecated=True)
def get_img(filename: str):
    filepath = os.path.join('images/', os.path.basename(filename))
    return FileResponse(filepath)


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
