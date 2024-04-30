from typing import Annotated, Optional
from pydantic import BaseModel, Field, BeforeValidator
from bson.objectid import ObjectId
from typing import Annotated, Optional
from pydantic import BaseModel, EmailStr, ConfigDict


class User(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "email": "string",
                "name": "string",
                "password": "string"
            }
        },
    )

# class User(BaseModel):
#     id: Optional[PyObjectId] = Field(alias="id", description="User id", default=None)
#     name: str
#     email: str
#     password: str
#
# class Config:
#     arbitrary_types_allowed = True
#     json_encoders = {ObjectId: str}
#     json_schema_extra = {"type": "object",
#                          "properties":
#                              {
#                                  "id": {"type": "string"},
#                                  "email": {"type": "string"},
#                                  "name": {"type": "string"},
#                                  "password": {"type": "string"}
#                              }}
