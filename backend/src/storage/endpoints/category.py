from typing import List, Optional
from tortoise.contrib.fastapi import HTTPNotFoundError
from .. import schemas, services
from src.users.routers import get_current_superuser
from fastapi import APIRouter, Depends


category_router = APIRouter(dependencies=[Depends(get_current_superuser)])


@category_router.get("/", response_model=List[schemas.GetCategory])
async def get_category(limit: Optional[int] = None, offset: Optional[int] = None):
    return await services.category_s.filter(limit=limit, offset=offset)


@category_router.get(
    "/{pk}", response_model=schemas.GetCategory,
    responses={404: {"model": HTTPNotFoundError}})
async def get_category_detail(pk: int):
    return await services.category_s.get(id=pk)


@category_router.delete(
    "/{pk}", responses={404: {"model": HTTPNotFoundError}}
)
async def delete_category(pk: int):
    await services.category_s.delete(id=pk)
    return {'status': True}


@category_router.post(
    "/", response_model=schemas.GetCategory,
    responses={404: {"model": HTTPNotFoundError}})
async def post_category(schema: schemas.CreateCategory):
    return await services.category_s.create(schema=schema)


@category_router.put(
    "/{pk}", response_model=schemas.GetCategory,
    responses={404: {"model": HTTPNotFoundError}})
async def put_category(pk: int, item: schemas.CreateCategory):
    return await services.category_s.update(id=pk, schema=item)
