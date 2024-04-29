from pydantic import BaseModel


class Ticket(BaseModel):
    start_date: str
    end_date: str
    category: str
