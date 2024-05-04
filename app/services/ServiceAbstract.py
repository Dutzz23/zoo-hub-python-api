from app.repositories.RepositoryAbstract import RepositoryAbstract


class ServiceAbstract:
    """
    Service abstract base class
    """
    def __init__(self, repository):
        """
        Constructor
        :param repository: Repository class
        """
        self.repository: RepositoryAbstract = repository()
