# Just copy-paste README.md here
# It's used the same format. (I cannot find a way to read it and use inside the docs)
description = """
## Project phase:
### `Development`
## Project Status:
### `WIP`

Python API using `FastAPI` and `MongoDB` for uni project.

Used `Redis` as cache system and `Pydantic` for object-modeling.

### Technologies

<span>
<img app="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" height="100" width="auto" alt="FastAPI logo">
&nbsp;<img app="https://upload.wikimedia.org/wikipedia/commons/9/93/MongoDB_Logo.svg" height="100" width="auto" 
alt="MongoDB Logo">&nbsp;&nbsp;
<img app="https://www.svgrepo.com/show/303460/redis-logo.svg" height="100" width="auto" alt="Redis Logo">
</span>
<br/>
<span>
<img app="https://www.sequoiacap.com/wp-content/uploads/sites/6/2023/08/name-and-logo-path.svg" height="100"
width="auto" alt="Pydantic Logo">&nbsp;&nbsp;
<img app="http://localhost:8000/img/jwt-seeklogo.svg" height="100" width="auto" alt="JWT Logo">
</span>

All API documentation can be viewed using [FastAPI auto-generated documentation](http://localhost:8000/docs),
or [Redoc](http://localhost:8000/redoc)


For local running:
```console
$ uvicorn main:app --host 0.0.0.0 --port 8000
``` 

***

## Future development requirements

- For defining new routes that returns collections, if you want to create a Schema (Pydantic model) for `FastApi` 
  auto-generated docs, please consult other collection definitions (from `./models`): the only attribute should be 
  `items` and named like that, for compatibility with RepositoryAbstract
- Use PyObjectId from `./utils` for `FastApi`/`MongoDB` for compatibility between both libraries
- define id field as below for renaming it from '_id' to 'id' (specify `validation_alias` or at least `alias`, that
  supports both validation and serialization)
```python
class Model(BaseModel):
    id: PyObjectId = Field(validation_alias="_id", title="id", description="Resource id. Alias: `id`")
```

***

## Observations

- Default `bson` lib interferes with `pydantic`. Used 'pybison' instead.
- PyObjectId from `./utils` is custom `ObjectId` so that `FastApi` can handle it on request (compatibility with `mongoDB` lib)
"""

description_old = """
## Project Status: WIP

Python API using FastAPI and MongoDB for uni project
All API documentation can be viewed on [Localhost](http://localhost:8000/docs)

<span color="red">shiny</span>

For local running:
```console
$ uvicorn main:app --host 0.0.0.0 --port 8000
``` 

***

## Future development requirements

## Future development requirements

- For defining new routes that returns collections, if you want to create a Schema (Pydantic model) for `FastApi` 
  auto-generated docs, please consult other collection definitions (from `./models`): the only attribute should be 
  `items` and named like that, for compatibility with RepositoryAbstract
- Use PyObjectId from `./utils` for `FastApi`/`MongoDB` for compatibility between both libraries
- define id field as below for renaming it from '_id' to 'id' (specify `validation_alias` or at least `alias`, that
  supports both validation and serialization)
    ```python
    class Model(BaseModel):
        id: PyObjectId = Field(validation_alias="_id", title="id", description="Resource id. Alias: `id`")
    ```

***

## Observations

- Default `bson` lib interferes with `pydantic`. Used 'pybison' instead.
- PyObjectId from `./utils` is custom `ObjectId` so that `FastApi` can handle it on request (compatibility with `mongoDB` lib)
"""
