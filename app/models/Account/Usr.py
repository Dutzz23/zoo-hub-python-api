from typing import Optional

from pydantic import BaseModel, EmailStr, ConfigDict, Field, constr, ValidationError, model_validator

from app.utils.PyObjectId import PyObjectId


class Usr(BaseModel):
    """
    User authentication model
    """
    id: Optional[PyObjectId] = Field(alias='_id')
    username: str
    password: str
    # username: str = Field(...)
    # password: str = Field(...)
    # password: constr(
    #     min_length=8,
    #     max_length=32,
    # ) = Field(...)
    #
    # @model_validator(mode='after')
    # def after(cls, v):
    #     pwd = str(v.dict()['password'])
    #     if len(pwd) < 8:
    #         raise ValidationError('Password must be at least 8 characters long')
    #     if len(pwd) > 32:
    #         raise ValidationError('Password must be less than 32 characters long')
    #     if not any(c.isupper() for c in pwd):
    #         raise ValueError("Password must have at least one uppercase letter")
    #     if not any(c.islower() for c in pwd):
    #         raise ValueError("Password must have at least one lowercase letter")
    #     if not any(c.isdigit() for c in pwd):
    #         raise ValueError("Password must have at least one digit")
    #     return v
    #
    # model_config = ConfigDict(
    #     populate_by_name=True,
    #     arbitrary_types_allowed=True,
    #     json_schema_extra={
    #         "title": "User authentication data",
    #         "example": {
    #             "username": "string",
    #             "password": "string"
    #         },
    #         "required": [
    #             "username",
    #             "password"
    #         ],
    #         "additionalProperties": False
    #     }
    # )
