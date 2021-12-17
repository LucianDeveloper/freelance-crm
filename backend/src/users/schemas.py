from fastapi_users import models
from tortoise import Tortoise
from tortoise.contrib.pydantic import PydanticModel
from fastapi_users.db import TortoiseUserDatabase
from config import db_paths
from src.users.models import UserModel
from typing import Optional
from pydantic import UUID4
from ..telegram.schemas import GetTGUserMinimize


Tortoise.init_models(db_paths.all_paths, 'models')


class User(models.BaseUser):
    first_name: str
    last_name: str
    patronymic_name: Optional[str] = None
    inn: int
    tg_account_id: Optional[int] = None
    is_verified: bool


class UserCreate(models.BaseUserCreate):
    first_name: str
    last_name: str
    patronymic_name: Optional[str] = None
    inn: int
    tg_account_id: Optional[int] = None


class UserUpdate(models.BaseUserUpdate):
    first_name: str
    last_name: str
    patronymic_name: Optional[str] = None
    inn: int
    tg_account_id: Optional[int] = None


class UserDB(User, models.BaseUserDB, PydanticModel):
    class Config:
        orm_mode = True
        orig_model = UserModel


def get_user_db():
    yield TortoiseUserDatabase(UserDB, UserModel)


class GetMinimizeUser(PydanticModel):
    id: UUID4
    email: str
    tg_account: Optional[GetTGUserMinimize] = None
    tg_account_id: Optional[int] = None
    first_name: str
    last_name: str
    patronymic_name: Optional[str] = None
    is_superuser: bool
    is_verified: bool

    class Config:
        orig_model = UserModel
