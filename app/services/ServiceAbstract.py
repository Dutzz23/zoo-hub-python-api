from app.repositories.RepositoryAbstract import RepositoryAbstract


class ServiceAbstract:
    def __init__(self, repository):
        self.repository: RepositoryAbstract = repository()
