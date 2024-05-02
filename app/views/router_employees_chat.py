from fastapi import APIRouter, WebSocket

employees_chat_router = APIRouter(prefix='/chat', tags=['employees-chat'])


@employees_chat_router.get('')
def default():
    return "Chat router"


clients = []


# WebSocket route
@employees_chat_router.websocket("/{id}")
async def websocket_endpoint(websocket: WebSocket, id: str):
    await websocket.accept()
    clients.append(websocket)
    print(id)
    try:
        while True:
            message = await websocket.receive_text()
            # Broadcast received message to all connected clients
            for client in clients:
                await client.send_text(message)
    finally:
        # Remove disconnected client from the list
        clients.remove(websocket)
