from typing import Optional, List

from bson import ObjectId
from pydantic import BaseModel

from app.utils.database.config import database


class RepositoryAbstract:
    def __init__(self, table_name: str, resource_class):
        self.collection = database[table_name]
        self.resource_class = resource_class
        self.collection_keys = self.resource_class.__fields__.keys()

    class Collection(BaseModel):
        """
           A container holding a list of `resource` instances.

           This exists because providing a top-level array in a JSON response can be a [vulnerability](https://haacked.com/archive/2009/06/25/json-hijacking.aspx/)
           """
        items: List[BaseModel]

    def create(self, data: BaseModel) -> Optional[str]:
        """
        Create a new resource (persist in the database).
        """
        try:
            data_dict = data.dict(exclude={"id"})  # Exclude the id field
            result = self.collection.insert_one(data_dict)
            return str(result.inserted_id)
        except Exception as e:
            print("RepositoryAbstract.create(): ", e)
        return None

    def find_by_id(self, data_id: str) -> Optional[BaseModel]:
        """
        Find a resource by its ID.
        """
        try:
            data = self.collection.find_one({'_id': ObjectId(data_id)})
            return self.resource_class(**data) if data else None
        except Exception as e:
            print("RepositoryAbstract.find_by_id(): ", e)
        return None

    def find_one_by(self, query: dict) -> Optional[BaseModel]:
        """
        Find a resource in the database based on the provided query.
        """
        try:
            if len(query.items()) == 0:
                raise ValueError("Query must have at least one key")
            for query_key in query.keys():
                if query_key not in self.collection_keys:
                    raise ValueError(f"Query key [{query_key}]is not part of collection")
            data = self.collection.find_one(query)
            return self.resource_class(**data) if data else None
        except Exception as e:
            print("RepositoryAbstract.find_one_by(): ", e)
        return None

    def find_all(self) -> Optional[Collection]:
        """
        Retrieve all resources as a List (limit=100).
        """
        try:
            data_list = self.collection.find().limit(100)
            items = [self.resource_class(**item) for item in data_list]
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

        try:
            result = self.collection.update_one({"_id": data.id}, {"$set": updated_fields})
            return result.modified_count > 0
        except Exception as e:
            print("RepositoryAbstract.update(): ", e)
        return False

    def delete(self, data_id: str) -> bool:
        """
        Delete a resource by its ID.
        """
        try:
            result = self.collection.delete_one({"_id": ObjectId(data_id)})
            return result.deleted_count > 0
        except Exception as e:
            print("RepositoryAbstract.delete(): ", e)
        return False
