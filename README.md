# ZooHub API

***

## Project phase:

### `Development`

***

## Project Status:

### `WIP`

***
Python API using `FastAPI` and `MongoDB` for uni project.

Used `Redis` as cache system and `Pydantic` for object-modeling.

Secure endpoints using "JWT" tokens.

### Technologies

<span>
<img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" height="100" width="auto" alt="FastAPI logo">
&nbsp;<img src="https://upload.wikimedia.org/wikipedia/commons/9/93/MongoDB_Logo.svg" height="100" width="auto" alt="MongoDB Logo">&nbsp;&nbsp;&nbsp;
<img src="https://www.svgrepo.com/show/303460/redis-logo.svg" height="100" width="auto" alt="Redis Logo>"><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://www.sequoiacap.com/wp-content/uploads/sites/6/2023/08/name-and-logo-path.svg" height="80" width="auto" alt="Pydantic Logo">&nbsp;&nbsp;
<img src="images/jwt-seeklogo.svg" height="80" width="auto" alt="JWT Logo"></span>

[//]: # (<img src="https://avatars.githubusercontent.com/u/110818415?s=100&v=4" height="100" width="auto" alt="Pydantic Logo">)

[//]: # (<img src="https://seeklogo.com/images/J/jwt-logo-11B708E375-seeklogo.com.png" height="100" width="auto" alt="JWT Logo">)
All of the API documentation can be viewed using [FastAPI auto-generated documentation](http://localhost:8000/docs),
or [Redoc](http://localhost:8000/redoc)
***

### Instructions for local running:

- Install Python. Check [Python installation documentation](https://www.python.org/downloads/)
- Install Redis on a Linux system/container (Use WSL for Windows).
  Check [Redis installation documentation](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/)
- Install project dependencies from `requirements.txt`
- Run Redis server in Linux terminal:
  ```console
  $ redis-server
  ```
- Start API:
  ```console
  $ uvicorn main:app --host 0.0.0.0 --port 8000
  ``` 

***

## Future development requirements

- For defining new routes that returns collections, if you want to create a Schema (Pydantic model) for `FastApi`
  auto-generated docs, please consult other
  collection definitions (from `./models`): the only attribute should be `items` and named like that, for compatibility
  with
  RepositoryAbstract
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
- PyObjectId from `./utils` is custom `ObjectId` so that `FastApi` can handle it on request (compatibility
  with `mongoDB` lib)


