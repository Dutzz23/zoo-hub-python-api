from pydantic import BaseModel, EmailStr, ConfigDict, Field

from src.utils.PyObjectId import PyObjectId


class UserData(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
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
