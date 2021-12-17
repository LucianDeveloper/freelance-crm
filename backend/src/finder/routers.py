from fastapi import APIRouter
from .schemas import SchemaFilterProducts, GetResponseProducts
from .services import Finder


finder_router = APIRouter()


@finder_router.get('/', response_model=GetResponseProducts)
async def get_products(schema: SchemaFilterProducts):
    return await Finder.get_products_by_filter(filters=schema)
