class SchemaAbstract:
    def __init__(self, schema_attributes: list[str]):
        self.schema_attributes = schema_attributes

    def map_from_schema(self, schema) -> dict:
        result = {element: schema[element] for element in self.schema_attributes}
        result['id'] = str(schema['_id'])
        return result

    def map_to_schema(self, entity_object) -> object:
        for attribute in self.schema_attributes:
            setattr(entity_object, attribute, getattr(entity_object, attribute))
        return entity_object
