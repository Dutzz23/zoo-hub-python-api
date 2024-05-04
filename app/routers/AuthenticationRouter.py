from typing import Annotated, Any
from urllib.request import Request

from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_framework import redis_dependency

from app.models.Account.AccountCollection import AccountCollection
from app.models.Account.Usr import Usr
from app.models.Auth.Token import Token
from app.services.AuthenticationService import AuthenticationService
from app.utils.generate_router_description import generate_router_description

AuthenticationRouter = APIRouter(prefix="/auth", tags=['Authentication'])

_service = AuthenticationService()


@AuthenticationRouter.post(
    path="/token",
    summary="Login",
    description="Token authentication using OAuth2 protocol (Login)",
    response_model=Token,
)
async def login(login_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    try:
        user = _service.authorise(login_data.username, login_data.password)
        if not user:
            raise Exception("Invalid credentials")
        access_token = _service.create_token(user.username)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Authentication error -> {e}",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return Token(access_token=access_token, token_type="bearer")


@AuthenticationRouter.post(
    path="/register",
    summary="Register",
    description="Register a new user",
    response_model=Token
)
async def register(register_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    try:
        user = _service.authenticate(register_data.username, register_data.password)
        if not user:
            raise Exception("Register failed")
        access_token = _service.create_token(user.username)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Authorization error -> {e}",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return Token(access_token=access_token, token_type="bearer")


@AuthenticationRouter.post(
    path='/accounts',
    summary="List all users",
    description="List all users as Collection",
    response_model=AccountCollection,
    response_model_by_alias=False,
    dependencies=[Depends(_service.verify_token)],
)
def get_all_accounts(user: Annotated[Usr, Depends(_service.verify_token)]) -> HTTPException | Any:
    try:
        rd = redis_dependency.redis.get('vlad')
        print("from endpooint method: ", rd)

        data = _service.get_all()
        return data
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))


@AuthenticationRouter.get(
    path='/account/{account_id}',
    summary="Get account by id",
    description="Get a specific account by id",
    dependencies=[Depends(_service.verify_token)],
)
async def get_account_by_id(account_id: str):
    try:
        data = _service.get_by_id(account_id)
        print("GET", data)
        return data
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))


@AuthenticationRouter.delete(
    path='/account/{account_id}',
    summary="Delete account by id",
    description="Delete a specific account by id `WIP`",
    dependencies=[Depends(_service.verify_token)],
)
async def delete_account_by_id(account_id: str):
    pass


@AuthenticationRouter.put(
    path='/account/{account_id}/change_password',
    summary="Change password",
    description="Change password `WIP`",
    dependencies=[Depends(_service.verify_token)],
)
def change_password(account_id: str, password: str):
    pass


@AuthenticationRouter.options(
    path="",
    description="Get Authentication router description (JSON)",
    summary="Router description",
    dependencies=[Depends(_service.verify_token)],
)
async def get_options():
    router_details = generate_router_description(AuthenticationRouter)
    return router_details
