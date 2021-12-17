from typing import Optional
from tortoise import Tortoise
from tortoise.contrib.pydantic import PydanticModel
from .models import Client
from ..telegram.schemas import GetTGUserMinimize
from config import DBPaths


Tortoise.init_models(DBPaths.clients, 'models')


class CreateClient(PydanticModel):
    fio: str
    phone: str
    url_tg: Optional[str] = None
    url_inst: Optional[str] = None
    tg_user_id: Optional[int] = None

    class Config:
        orig_model = Client


class GetClient(CreateClient):
    id: int
    tg_user: Optional[GetTGUserMinimize] = None
