from typing import Optional
from pydantic import Field, EmailStr, ConfigDict, BaseModel
from bson import ObjectId

from app.models.User.UserData import UserData
from app.utils.PyObjectId import PyObjectId


class User(BaseModel):
    """
    User model
    """
    id: PyObjectId = Field(validation_alias="_id", title="id", description="User id. Alias: `id`")
    name: Optional[str] = Field(description="User name")
    email: Optional[EmailStr] = Field(description="User email")
    password: Optional[str] = Field(description="User password")

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        populate_by_name=True,
        json_schema_extra={
            "title": "User Data uwu",
            "example": {
                "name": "string",
                "email": "string",
                "password": "string"
            },
            "required": [
                "name",
                "email",
                "password"
            ],
            "additionalProperties": False
        }
    )
