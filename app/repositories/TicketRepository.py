from app.models.entities.TicketEntity import TicketEntity
from app.repositories.RepositoryAbstract import RepositoryAbstract


class TicketRepository(RepositoryAbstract):
    def __init__(self):
        super().__init__("tickets", TicketEntity)
