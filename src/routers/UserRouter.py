from http import HTTPStatus

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.models.User.User import User
from src.models.User.UserCollection import UserCollection
from src.utils.database.config import database
from src.models.User.UserData import UserData
from src.repositories.UserRepository import UserRepository

UserRouter = APIRouter(prefix='/users', tags=['users'])

collection = database['users']

repository = UserRepository()


@UserRouter.get(
    path='',
    response_description="List all users",
    response_model=UserCollection,
    response_model_by_alias=False,
)
async def get_users():
    """
            A list of `User` records will be provided in the response.
    """
    users = repository.read_all_users()
    return users


# users = collection.find()
# l = []
# for user in users:
#     print(User(**user))
#     l.append(User(**user))
# return l


@UserRouter.post(
    path='',
    response_model=UserData,
    response_description="Create a new user",
    status_code=HTTPStatus.CREATED,
    response_model_by_alias=False
)
async def create_user(user: UserData):
    """
        Insert a new user record.
        A unique `id` will be created and provided in the response.
    """
    # Remove the id field from the user object
    # new_user = collection.insert_one(user.model_dump(by_alias=True, exclude=set("id")))
    new_user_id = repository.create_user(user)
    # created_user = collection.find_one({"id": new_user.inserted_id})
    if new_user_id is not None:
        created_user = repository.read_user_by_id(new_user_id)
        return created_user
    return JSONResponse(status_code=404, content=f"User cannot be created")

    # user_dict = user.dict(exclude={'id'})
    #
    # # Insert the user into the database
    # result = collection.insert_one(user_dict)
    # created_user = collection.find_one({"_id": result.inserted_id})
    #
    # if created_user:
    #     return "User created successfully"
    # else:
    #     raise HTTPException(status_code=500, detail="Error creating user")


@UserRouter.get(
    path="/{user_id}",
    response_description="Get a user by id",
    response_model=User,
    response_model_by_alias=False,
    responses={404: {"description": "Not found"}},
)
async def read_user(user_id: str):
    user: User = repository.read_user_by_id(user_id)
    if user is not None:
        print("user in read_user", user)
        return user
    else:
        return JSONResponse(status_code=404, content=f"User with id={user_id} not found")

# @UserRouter.post("/users/")
# async def create_user(user: User):
#     # Convert Pydantic model to dictionary for MongoDB insertion
#     user_data = user.dict(exclude_unset=True)
#     result = collection.insert_one(user_data)
#     inserted_id = result.inserted_id
#     return {"id": str(inserted_id), **user_data}

#
# @UserRouter.get("/users/{user_id}")
# async def read_user(user_id: str):
#     mongo_user = collection.find_one({"_id": ObjectId(user_id)})
#     if mongo_user:
#         return User(**mongo_user)
#     else:
#         raise HTTPException(status_code=404, detail="User not found")
#
#
# @UserRouter.put("/users/{user_id}")
# async def update_user(user_id: str, user: User):
#     # Convert Pydantic model to dictionary for MongoDB update
#     user_data = user.dict(exclude_unset=True)
#     result = collection.update_one({"_id": ObjectId(user_id)}, {"$set": user_data})
#     if result.modified_count:
#         return {"message": "User updated successfully"}
#     else:
#         raise HTTPException(status_code=404, detail="User not found")
#
#
# @UserRouter.delete("/users/{user_id}")
# async def delete_user(user_id: str):
#     result = collection.delete_one({"_id": ObjectId(user_id)})
#     if result.deleted_count:
#         return {"message": "User deleted successfully"}
#     else:
#         raise HTTPException(status_code=404, detail="User not found")
