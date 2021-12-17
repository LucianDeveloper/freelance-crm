from aiohttp import ClientSession

from ..telegram.models import TGUser
from .schemas import SendMessage
from .models import BroadcastHistory

from config import TOKEN_TG


async def send_broadcast(schema: SendMessage):
    count_success = 0
    count_all = 0
    async with ClientSession() as session:
        if schema.lang_id is None:
            query = TGUser.all()
        else:
            query = TGUser.filter(lang_id=schema.lang_id)
        for user in await query:
            async with session.get(
                    f'https://api.telegram.org/bot{TOKEN_TG}/sendMessage',
                    params={
                        'chat_id': user.id,
                        'text': schema.text
                    }
            ) as response:
                count_all += 1
                if response.ok:
                    count_success += 1
    await BroadcastHistory.create(
        count_all=count_all,
        count_success=count_success,
        text=schema.text
    )
