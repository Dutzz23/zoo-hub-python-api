from src.models.Account.Usr import Usr
from src.repositories.RepositoryAbstract import RepositoryAbstract


class UsrRepository(RepositoryAbstract):
    def __init__(self):
        super().__init__("users", Usr)
