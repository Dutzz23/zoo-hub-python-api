from app.models.Account.Usr import Usr
from app.repositories.RepositoryAbstract import RepositoryAbstract


class UsrRepository(RepositoryAbstract):
    def __init__(self):
        super().__init__("users", Usr)
