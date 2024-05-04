from datetime import timedelta, datetime, timezone
from io import BytesIO

from app.models.schemas.Ticket import Ticket
from app.repositories.TicketRepository import TicketRepository
from app.services.ServiceAbstract import ServiceAbstract
from qrcode import make as make_qrcode


class TicketService(ServiceAbstract):
    def __init__(self):
        super().__init__(TicketRepository)

    async def generate_ticket(self, ticket: Ticket):
        try:
            qrcode = make_qrcode(ticket.model_dump_json())
            ticket.billing_date = datetime.now(timezone.utc)
            qrcode_buffer = BytesIO()
            self.repository.create(ticket)
            qrcode.save(qrcode_buffer, kind='png')
            qrcode_buffer.seek(0)
            return qrcode_buffer
        except Exception as e:
            raise e

    def scan_ticket(self, ticket: Ticket):
        if ticket.billing_date + timedelta(weeks=4) < datetime.now(timezone.utc):
            raise Exception("Ticket expired")
        try:
            self.repository.find_by_id(ticket.id)
        except Exception as e:
            raise Exception("Ticket not found")
        try:
            self.repository.delete(ticket.id)
        except Exception as e:
            raise Exception("Error deleting ticket")
        return ticket
