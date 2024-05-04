from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class TicketOptions(BaseModel):
    """
    Ticket options representation for purchasing different number of tickets for a certain visitor type
    """
    regulars: Optional[int] = Field(description="Number of tickets for regulars", default=0, ge=0, lt=100)
    students: Optional[int] = Field(description="Number of tickets for students", default=0, ge=0, lt=100)
    children: Optional[int] = Field(description="Number of tickets for children", default=0, ge=0, lt=100)

    model_config = ConfigDict(
        arbitrary_types_allowed=False,
        populate_by_name=True,
        json_schema_extra={
            "title": "Ticket data",
            "example": {
                "regulars": 0,
                "students": 0,
                "children": 0
            },
            "required": None,
            "additionalProperties": False
        }
    )
