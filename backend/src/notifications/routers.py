from fastapi import APIRouter
from .schemas import SendMessage
from . import services


notify_router = APIRouter()


@notify_router.post('', name='Endpoint для отправки уведомлений от системы пользователям бота')
async def send_notify(schema: SendMessage):
    await services.send_notifications(schema)
