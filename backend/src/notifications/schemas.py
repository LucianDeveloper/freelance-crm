from pydantic import BaseModel
from tortoise import Tortoise
from config import DBPaths


Tortoise.init_models(DBPaths.notifications, 'models')


class SendMessage(BaseModel):
    user_id: int
    text: str
