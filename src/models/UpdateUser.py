from typing import Optional
from pydantic import BaseModel, Field, EmailStr, ConfigDict, model_validator
from bson import ObjectId

from src.utils.PyObjectId import PyObjectId


class UpdateUser(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", title="id", description="User id")
    name: Optional[str] = Field(alias="name", description="User name")
    email: Optional[EmailStr] = Field(alias="email", description="User email")
    password: Optional[str] = Field(alias="password", description="User password")

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        populate_by_name=True
    )
