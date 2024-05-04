from app.schemas.ShemaAbstract import SchemaAbstract


class UserSchema(SchemaAbstract):
    def __init__(self):
        schema_attributes = ["name", "email", "password"]
        SchemaAbstract.__init__(self, schema_attributes)
