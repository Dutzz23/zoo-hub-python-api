from typing import Annotated, Any

from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from src.models.Account.AccountCollection import AccountCollection
from src.models.Account.Usr import Usr
from src.models.Auth.Token import Token
from src.services.AuthenticationService import AuthenticationService


AuthenticationRouter = APIRouter(tags=['Authentication'])

_service = AuthenticationService()


@AuthenticationRouter.post("/token")
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


@AuthenticationRouter.post("/register")
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
    response_model=AccountCollection,
    response_model_by_alias=False,
)
def get_all_accounts(user: Annotated[Usr, Depends(_service.verify_token)]) -> HTTPException | Any:
    try:
        _service.repository.find_one_by({"email": "dsdasd@mail.com"})
        data = _service.get_all()
        print("GET ALL", data)
        return data
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))


@AuthenticationRouter.get('/account/{account_id}')
async def get_account_by_id(account_id: str):
    try:
        data = _service.get_by_id(account_id)
        print("GET", data)
        return data
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))


@AuthenticationRouter.delete('/account/{account_id}')
async def delete_account_by_id(account_id: str):
    pass


@AuthenticationRouter.put('/account/{account_id}/change_password')
def change_password(account_id: str, password: str):
    pass
