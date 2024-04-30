from src.utils.database.config import database


class RepositoryAbstract:
    def __init__(self, table_name: str, schema):
        self.collection = database[table_name]
        self.schema = schema
