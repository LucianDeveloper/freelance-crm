from typing import List, Optional
from tortoise.contrib.fastapi import HTTPNotFoundError
from src.telegram import schemas, services
from fastapi import APIRouter


tg_user_router = APIRouter()


@tg_user_router.get("/", response_model=List[schemas.GetTGUser])
async def get_tg_users(limit: Optional[int] = None, offset: Optional[int] = None):
    return await services.tg_user_s.filter(limit=limit, offset=offset)


@tg_user_router.get(
    "/{pk}", response_model=schemas.GetTGUser,
    responses={404: {"model": HTTPNotFoundError}})
async def get_tg_user_detail(pk: int):
    return await services.tg_user_s.get(id=pk)


@tg_user_router.delete(
    "/{pk}", responses={404: {"model": HTTPNotFoundError}}
)
async def delete_tg_user(pk: int):
    await services.tg_user_s.delete(id=pk)
    return {'status': True}


@tg_user_router.post(
    "/", response_model=schemas.GetTGUser,
    responses={404: {"model": HTTPNotFoundError}})
async def post_tg_user(schema: schemas.CreateTGUser):
    return await services.tg_user_s.create(schema=schema)


@tg_user_router.put(
    "/{pk}", response_model=schemas.GetTGUser,
    responses={404: {"model": HTTPNotFoundError}})
async def put_tg_user(pk: int, item: schemas.UpdateTGUser):
    return await services.tg_user_s.update(id=pk, schema=item)


@tg_user_router.post(
    "/code", responses={404: {"model": HTTPNotFoundError}})
async def get_code(schema: schemas.SchemaPhone):
    return await services.tg_user_s.get_code(schema=schema)
