from tortoise.contrib.pydantic import pydantic_model_creator, PydanticModel
from src.languages.models import Phrase
from config import DBPaths
from tortoise import Tortoise


Tortoise.init_models(DBPaths.languages, 'models')


class GetPhrase(PydanticModel):
    id: int
    code: str
    text: str

    class Config:
        orig_model = Phrase


class UpdatePhrase(PydanticModel):
    text: str

    class Config:
        orig_model = Phrase
