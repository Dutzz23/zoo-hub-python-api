from typing import Optional, List, Generic, TypeVar

from bson import ObjectId
from pydantic import BaseModel

from src.utils.database.config import database

T = TypeVar('T')


class RepositoryAbstract(Generic[T]):
    def __init__(self, table_name: str, resource_class):
        self.collection = database[table_name]
        self.resource_class = resource_class

    def get_resource_class(self):
        return self.resource_class

    class Collection(BaseModel):
        """
           A container holding a list of resource` instances.

           This exists because providing a top-level array in a JSON response can be a [vulnerability](https://haacked.com/archive/2009/06/25/json-hijacking.aspx/)
           """
        items: List[T]

    def create(self, data: BaseModel) -> Optional[str]:
        """
        Create a new resource (persist in the database).
        """
        try:
            data_dict = data.dict(exclude={"id"})  # Exclude the id field
            # data_dict = data.dict(show_secrets=False)
            result = self.collection.insert_one(data_dict)
            return str(result.inserted_id)
        except Exception as e:
            print(e)
        return None

    def read_by_id(self, data_id: str) -> Optional[BaseModel]:
        try:
            data = self.collection.find_one({'_id': ObjectId(data_id)})
            print("Data from abstract repo", data)
            return self.resource_class(**data)
        except Exception as e:
            print(e)
        return None

    def read_all(self) -> Optional[Collection]:
        """
        Retrieve all resources as a List (limit=100).
        """
        try:
            data_list = self.collection.find().limit(100)
            print("Data from abstract repo", data_list)
            items = [self.resource_class(**item) for item in data_list]
            print("items", items)
            return self.Collection(items=items)
            # return data_list
        except Exception as e:
            print("RepositoryAbstract.read_all(): ", e)
        return None

    def update(self, data: BaseModel) -> bool:
        """
        Update a resource (persist in the database).
        """
        updated_fields = {}

        for key, value in data.dict(exclude={"id"}).items():
            if value is not None:
                updated_fields[key] = value

        # Update the resource in the database
        try:
            result = self.collection.update_one({"_id": data.id}, {"$set": updated_fields})
            return result.modified_count > 0
        except Exception as e:
            print(e)
        return False

    def delete(self, data_id: str) -> bool:
        """
        Delete a resource by its ID.
        """
        try:
            result = self.collection.delete_one({"_id": ObjectId(data_id)})
            return result.deleted_count > 0
        except Exception as e:
            print(e)
        return False
