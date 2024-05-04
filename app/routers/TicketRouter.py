import base64
from typing import Annotated

from fastapi import APIRouter, Depends

from app.models.Account.Usr import Usr
from app.models.schemas.Ticket import Ticket
from app.services.AuthenticationService import AuthenticationService
from app.services.TicketService import TicketService
from app.utils.generate_router_description import generate_router_description

TicketRouter = APIRouter(prefix='/tickets', tags=['Tickets'])

_service = TicketService()
_authentication_service = AuthenticationService()

@TicketRouter.post(
    path='/purchase',
    name='Purchase Ticket',
    summary='Purchase Ticket',
    description='Purchase ticket',
    dependencies=[Depends(_authentication_service.verify_token)],
)
async def create_ticket(ticket: Ticket):
    try:
        image = await _service.generate_ticket(ticket)
        #     return Response(content=image.getvalue(), media_type="image/png")
        return {
            'image': base64.b64encode(image.getvalue()).decode("utf-8"),
            'status': 'success'
        }
    except Exception as e:
        print("Return ERROR", e)


@TicketRouter.post(
    path='/scan',
    name='Scan Ticket',
    summary='Scan Ticket',
    description='Scan Ticket for validation',
    dependencies=[Depends(_authentication_service.verify_token)],
)
async def scan_ticket(ticket: Ticket):
    try:
        return _service.scan_ticket(ticket)
    except Exception as e:
        return Exception(f"Error while scanning ticket: {e}")


@TicketRouter.post(
    path='/refund',
    name='Refund Ticket',
    summary='Refund Ticket',
    description='Refund Ticket',
)
async def refund_ticket(ticket: Ticket):
    pass  # TODO


@TicketRouter.options(
    path="",
    description="Get Ticket router description (JSON)",
    summary="Router description",
)
async def get_options():
    router_details = generate_router_description(TicketRouter)
    return router_details

# Request with src for HTML <img/> and status
# @TicketRouter.get(
#     path='/purchase',
#     name='Purchase Ticket',
# )
# async def create_ticket():
#     try:
#         image = await _service.generate_ticket(Ticket(id="sd", name="sdf", options=TicketOptions()))
#         return {
#             'image': 'data:image/png;base64,' + base64.b64encode(image.getvalue()).decode("utf-8"),
#             'status': 'success'
#         }
#     except Exception as e:
#         print("Return ERROR", e)
