from typing import Optional, List
from pydantic import UUID4
from tortoise import Tortoise
from tortoise.contrib.pydantic import PydanticModel
from .models import Category, Product, Sale
from ..users.schemas import User
from ..clients.schemas import GetClient
from config import DBPaths


Tortoise.init_models(DBPaths.storage, 'models')


class CreateCategory(PydanticModel):
    name: str

    class Config:
        orig_model = Category


class GetCategory(CreateCategory):
    id: int


class CreateProduct(PydanticModel):
    title: str
    description: str
    count: Optional[int] = None
    cost: Optional[int] = None
    is_deleted: Optional[bool] = False
    category_id: int
    user_id: UUID4

    class Config:
        orig_model = Product


class GetProduct(CreateProduct):
    id: int
    category: GetCategory
    user: User


class CreateSale(PydanticModel):
    products_ids: List[int] = []
    client_id: int

    class Config:
        orig_model = Sale


class GetSale(CreateSale):
    id: int
    products: List[GetProduct] = []
    client: Optional[GetClient] = None
