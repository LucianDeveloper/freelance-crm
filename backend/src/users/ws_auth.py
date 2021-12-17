from fastapi import WebSocket
from .routers import cookie_authentication, get_user_db


async def websocket_auth(websocket: WebSocket):
    try:
        cookie = websocket._cookies['fastapiusersauth']
        user = await cookie_authentication(cookie, next(get_user_db()))
        if user and user.is_active:
            return user
        return None
    except:
        return None
