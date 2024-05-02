import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis import Redis
from redis.commands.search.field import TextField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from starlette.responses import FileResponse

from api_description import description
from src.routers.AuthenticationRouter import AuthenticationRouter
from src.routers.UserRouter import UserRouter

app = FastAPI(
    title="ZooHub API",
    description=description,
    version="0.1.0",
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

app.include_router(UserRouter)
app.include_router(AuthenticationRouter)



# noinspection PyTypeHints
@app.on_event("startup")
async def startup():
    global redis_cache
    redis_cache = Redis(host='localhost', port=6379, db=0)

    # schema = (
    #     TextField("$.username", as_name="username"),
    #     TextField("$.token", as_name="token"),
    # )
    #
    # redis_cache = redis_cache.ft("idx:users")
    # redis_cache.create_index(
    #     schema,
    #     definition=IndexDefinition(
    #         prefix=["user:"], index_type=IndexType.JSON
    #     )
    # )


    print("Redis connection established")


@app.on_event("shutdown")
async def shutdown():
    global redis_cache
    redis_cache.close()
    print("Redis connection ended")


# Route for FastApiDocs to display local images. Not to be exposed
@app.get(
    path="/img/{filename}",
    deprecated=True)
def get_img(filename: str):
    filepath = os.path.join('images/', os.path.basename(filename))
    return FileResponse(filepath)


@app.get("/")
async def root():
    try:
        pass
        # client.admin.command('ping')
        # print("output", client.zoo_hub_python_api_db.users.find())
        # print(users_entity(client.zoo_hub_python_api_db.users.find()))
        # return users_entity(client.zoo_hub_python_api_db.users.find())
        # user_repo = UserRepository()
        # data = client.zoo_hub_python_api_db.users.find()
        # s = UserSchema()
        # for user in data:
        #     print("USERACHE", user)
        # print(user_repo.collection)
        # return user_repo.get_all_users()
    except Exception as e:
        print(e)
    # return {"message": "Hello World"}


# @app.post("/new")
# async def new_user(user: User):
#     try:
#         client.admin.command('ping')
#         client.zoo_hub_python_api_db.users.insert_one(dict(user))
#         # print(users_entity(client.zoo_hub_python_api_db.users.find()))
#         # return users_entity(client.zoo_hub_python_api_db.users.find())
#     except Exception as e:
#         print(e)
#     # return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    try:
        global redis_cache
        redis_cache.set("hello", str(name))
        # print("LOL", redis_cache.get('vlad').decode("utf-8"))
        res = redis_cache.get('hello')
        print(str(str(res)))
    except Exception as e:
        print(e)
    return {"message": f"Hello {name}"}
