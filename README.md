# ZooHub API

## Project Status:
### WIP

Python API using FastAPI and MongoDB for uni project
All API documentation can be viewed on http://localhost:8000/docs

For local running:
```console
$ uvicorn main:app --host 0.0.0.0 --port 8000
``` 

***

## Future development requirements

- For defining new routes that returns collections, if you want to create a Schema (Pydantic model) for `FastApi` auto-generated docs, please consult other
  collection definitions (from `./models`): the only attribute should be `items` and named like that, for compatibility with
  RepositoryAbstract
- Use PyObjectId from `./utils` for `FastApi`/`MongoDB` for compatibility between both libraries
- define id field as below for renaming it from '_id' to 'id' (specify `validation_alias` or at least `alias`, that
  supports both validation and serialization)

```python
class Model(BaseModel):
    id: PyObjectId = Field(validation_alias="_id", title="id", description="User id. Alias: `id`")
```

***

## Observations

- Default `bson` lib interferes with `pydantic`
- PyObjectId from `./utils` is custom `ObjectId` so that `FastApi` can handle it on request (compatibility with `mongoDB` lib)


