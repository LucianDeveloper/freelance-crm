from typing import List, Optional
from fastapi import APIRouter
from tortoise.contrib.fastapi import HTTPNotFoundError
from . import schemas, services


clients_router = APIRouter()


@clients_router.get("/", response_model=List[schemas.GetClient])
async def get_clients(limit: Optional[int] = None, offset: Optional[int] = None):
    return await services.clients_s.filter(limit=limit, offset=offset)


@clients_router.get(
    "/{pk}", response_model=schemas.GetClient,
    responses={404: {"model": HTTPNotFoundError}})
async def get_client_detail(pk: int):
    return await services.clients_s.get(id=pk)


@clients_router.put(
    "/{pk}", response_model=schemas.GetClient,
    responses={404: {"model": HTTPNotFoundError}})
async def put_client(pk: int, schema: schemas.CreateClient,):
    return await services.clients_s.update(id=pk, schema=schema)


@clients_router.post('/', response_model=schemas.GetClient)
async def post_client(schema: schemas.CreateClient):
    return await services.clients_s.create(schema=schema)
