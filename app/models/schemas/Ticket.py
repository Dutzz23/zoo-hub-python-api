from datetime import datetime
from typing import Optional

from pydantic import Field, ConfigDict, BaseModel
from bson import ObjectId

from app.models.TicketOptions import TicketOptions
from app.utils.PyObjectId import PyObjectId


class Ticket(BaseModel):
    """
    Ticket model
    """
    name: str = Field(description="Name of the user who bought the ticket")
    is_paid: bool = Field(description="Whether the ticket is paid from web purchasing or not.", default=False)
    options: TicketOptions = Field(description="Options related to the ticket")
    # id: PyObjectId = Field(validation_alias='_id', title="id", description="Ticket id. Alias: `id`")
    # user_id: Optional[PyObjectId] = Field(default=None, title="user_id", description="User id`")
    # billing_date: Optional[datetime] = Field(default=None, title="billing_date", description="Billing date of the ticket")

    model_config = ConfigDict(
        json_encoders={ObjectId: str},
        populate_by_name=True,
        json_schema_extra={
            "title": "Ticket data",
        #TODO error over request
            "example": {
                "name": "string",
                "is_paid": False,
                "options": TicketOptions.model_json_schema()["example"]
            },
            "required": ["name", "is_paid", "options"],
        },
    )
