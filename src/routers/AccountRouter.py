from fastapi import APIRouter, HTTPException
from fastapi.openapi.models import Response

from src.models.Account.AccountCollection import AccountCollection
from src.services.AccountService import AccountService

AccountRouter = APIRouter(prefix="/acc", tags=['Account'])

_service = AccountService()


@AccountRouter.get('/login')
async def login():
    pass


@AccountRouter.get('/logout')
async def logout():
    pass


@AccountRouter.post('/register')
async def register():
    pass


@AccountRouter.get(
    path='/accounts',
    response_model=AccountCollection,
    response_model_by_alias=False,
    )
async def get_all_accounts():
    try:
        _service.repository.find_one_by({})
        data = _service.get_all()
        print("GET ALL", data)
        return data
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))

@AccountRouter.get('/{account_id}')
async def get_account_by_id(account_id: str):
    try:
        data = _service.get_by_id(account_id)
        print("GET", data)
        return data
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))