from typing import List

from pydantic import BaseModel

from app.models.User.User import User
from app.models.User.UserData import UserData


class UserCollection(BaseModel):
    """
       A container holding a list of `User` instances.

       This exists because providing a top-level array in a JSON response can be a [vulnerability](https://haacked.com/archive/2009/06/25/json-hijacking.aspx/)
       """
    users: List[User]
