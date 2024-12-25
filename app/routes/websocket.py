from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.services.nlp_processing import user_input


router = APIRouter()

sessions = {}

@router.websocket("/qa/")
async def qa_endpoint(websocket: WebSocket):
    await websocket.accept()
    session_context = []
    try:
        while True:
            data = await websocket.receive_text()
            response = user_input(data, session_context)
            session_context.append(data)  # Maintain context
            await websocket.send_text(response)
    except WebSocketDisconnect:
        print("WebSocket connection closed")
