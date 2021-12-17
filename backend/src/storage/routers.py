from fastapi import APIRouter
from .endpoints.category import category_router
from .endpoints.products import products_router


storage_router = APIRouter()


storage_router.include_router(category_router, prefix='/categories')
storage_router.include_router(products_router, prefix='/products')
