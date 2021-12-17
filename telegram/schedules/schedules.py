import asyncio
import aioschedule
from client.base import api
from utils.lang_selector import lang_selector


async def scheduler():
    # Update cookies for auth
    aioschedule.every(15).minutes.do(api.refresh_login)
    # Updating phrases
    task = aioschedule.every(5).minutes.do(lang_selector.update)
    await task.run()

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
