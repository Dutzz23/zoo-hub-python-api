from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers.UserRouter import UserRouter

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # allow_origins=["http://localhost:3000"],
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(UserRouter)


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
    return {"message": f"Hello {name}"}
