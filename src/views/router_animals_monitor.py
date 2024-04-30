from fastapi import APIRouter

animals_monitor_router = APIRouter(prefix='/monitor', tags=['monitor'])


@animals_monitor_router.get('/')
def myLittleFunc():
    return "Monitor router working!"
