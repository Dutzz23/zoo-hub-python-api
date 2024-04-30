from typing import Optional

from src.models.User.User import User
from src.models.User.UserData import UserData
from src.models.User.UserCollection import UserCollection
from src.utils.database.config import database
from bson import ObjectId


class UserRepository:
    def __init__(self):
        self.collection = database['users']

    def create_user(self, user: UserData) -> Optional[str]:
        """
        Create a new user.
        """
        try:
            user_dict = user.dict(exclude={"id"})  # Exclude the id field
            result = self.collection.insert_one(user_dict)
            return str(result.inserted_id)
        except Exception as e:
            print(e)
        return None

    def read_all_users(self) -> Optional[UserCollection]:
        """
        Retrieve all users (limit=100).
        """
        try:
            users = self.collection.find().limit(100)
            return UserCollection(users=users)
        except Exception as e:
            print(e)
        return None

    def read_user_by_id(self, user_id: str) -> Optional[User]:
        """
        Retrieve a user by their ID.
        """
        try:
            user = self.collection.find_one({'_id': ObjectId(user_id)})
            return user
        except Exception as e:
            print(e)
        return None

    def read_user_by_email(self, email: str) -> Optional[UserData]:
        """
        Retrieve a user by their email.
        """
        try:
            user = self.collection.find_one({"email": email})
            return UserData(**user)
        except Exception as e:
            print(e)
        return None

    def read_user_by_name(self, name: str) -> Optional[UserData]:
        """
        Retrieve a user by their name.
        """
        try:
            user = self.collection.find_one({"name": name})
            return UserData(**user)
        except Exception as e:
            print(e)
        return None

    def update_user(self, user: UserData) -> bool:
        """
        Update a user.
        """
        updated_fields = {}

        for key, value in user.dict(exclude={"id"}).items():
            if value is not None:
                updated_fields[key] = value

        # Update the user in the database
        try:
            result = self.collection.update_one({"_id": user.id}, {"$set": updated_fields})
            return result.modified_count > 0
        except Exception as e:
            print(e)
        return False

    def delete_user(self, user_id: str) -> bool:
        """
        Delete a user by their ID.
        """
        try:
            result = self.collection.delete_one({"_id": ObjectId(user_id)})
            return result.deleted_count > 0
        except Exception as e:
            print(e)
        return False
