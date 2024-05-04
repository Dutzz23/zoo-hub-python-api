from datetime import datetime
from typing import Optional
from pydantic import Field

from app.models.schemas.Ticket import Ticket
from app.utils.PyObjectId import PyObjectId


class TicketEntity(Ticket):
    id: PyObjectId = Field(validation_alias='_id', title="id", description="Ticket id. Alias: `id`")
    user_id: Optional[PyObjectId] = Field(default=None, title="user_id", description="User id`")
    billing_date: Optional[datetime] = Field(default=None, title="billing_date",
                                             description="Billing date of the ticket")
