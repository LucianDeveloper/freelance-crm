from typing import List, Optional
from tortoise.contrib.fastapi import HTTPNotFoundError
from .. import schemas, services
from src.users.routers import get_current_active_user
from fastapi import APIRouter, Depends


products_router = APIRouter(dependencies=[Depends(get_current_active_user)])


@products_router.get("/", response_model=List[schemas.GetProduct])
async def get_products(limit: Optional[int] = None, offset: Optional[int] = None):
    return await services.product_s.filter(limit=limit, offset=offset)


@products_router.get(
    "/{pk}", response_model=schemas.GetProduct,
    responses={404: {"model": HTTPNotFoundError}})
async def get_product_detail(pk: int):
    return await services.product_s.get(id=pk)


@products_router.delete(
    "/{pk}", responses={404: {"model": HTTPNotFoundError}}
)
async def delete_product(pk: int):
    await services.product_s.delete(id=pk)
    return {'status': True}


@products_router.post(
    "/", response_model=schemas.GetProduct,
    responses={404: {"model": HTTPNotFoundError}})
async def post_products(schema: schemas.CreateProduct):
    return await services.product_s.create(schema=schema)


@products_router.put(
    "/{pk}", response_model=schemas.GetProduct,
    responses={404: {"model": HTTPNotFoundError}})
async def put_products(pk: int, item: schemas.CreateProduct):
    return await services.product_s.update(id=pk, schema=item)
