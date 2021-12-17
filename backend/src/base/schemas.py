from tortoise.contrib.pydantic import PydanticModel
from .models import File
from config import db_paths, URL
from tortoise import Tortoise
from typing import Optional


Tortoise.init_models(db_paths.base, 'models')


class GetFile(PydanticModel):
    id: int
    url: str
    size: Optional[int] = None

    def __init__(self, **kwargs):
        super(GetFile, self).__init__(**kwargs)
        self.url = f'{URL}/{self.url}' if not self.url.startswith(URL) else self.url

    class Config:
        orig_model = File
