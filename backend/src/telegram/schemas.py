from pydantic import BaseModel

from config import DBPaths
from typing import Optional
from tortoise import Tortoise
from tortoise.contrib.pydantic import PydanticModel
from datetime import datetime

from .models import TGUser


Tortoise.init_models(DBPaths.telegram, 'models')


class UpdateTGUser(PydanticModel):
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None

    class Config:
        orig_model = TGUser


class CreateTGUser(UpdateTGUser):
    id: int


class GetTGUser(CreateTGUser):
    join_date: datetime
    join_date_formatted: Optional[str] = None

    def __init__(self, **kwargs):
        super(GetTGUser, self).__init__(**kwargs)
        self.join_date_formatted = self.join_date.strftime("%Y-%m-%d %H:%M:%S")


class GetTGUserMinimize(PydanticModel):
    id: int
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    class Config:
        orig_model = TGUser


class SchemaPhone(BaseModel):
    phone: str


class GetCode(BaseModel):
    code: str
