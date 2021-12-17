from pydantic import BaseModel
from tortoise import Tortoise
from config import DBPaths
from .models import BroadcastHistory
from typing import Optional


Tortoise.init_models(DBPaths.broadcast, 'models')


class SendMessage(BaseModel):
    text: str
    lang_id: Optional[int] = None
    # file_id: int
