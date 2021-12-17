from fastapi import HTTPException, status
from aiohttp import ClientSession

from ..telegram.models import TGUser
from .schemas import SendMessage
from .models import NotificationHistory

from config import TOKEN_TG


async def send_notifications(schema: SendMessage):
    if not await TGUser.exists(id=schema.user_id):
        await NotificationHistory.create(status=404)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Пользователь с этим ID не найден")
    async with ClientSession() as session:
        async with session.get(
                f'https://api.telegram.org/bot{TOKEN_TG}/sendMessage',
                params={
                    'chat_id': schema.user_id,
                    'text': schema.text,
                    'parse_mode': 'HTML'
                }
        ) as response:
            if not response.ok:
                await NotificationHistory.create(status=500)
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="При отправке случилась неизвестная ошибка"
                )
    await NotificationHistory.create(status=200)
    raise HTTPException(status_code=status.HTTP_200_OK, detail="Сообщение отправлено")
