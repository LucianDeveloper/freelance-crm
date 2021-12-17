from typing import List, Optional
from fastapi import APIRouter
from tortoise.contrib.fastapi import HTTPNotFoundError
from src.languages import schemas, services


phrases_router = APIRouter()


@phrases_router.get("/", response_model=List[schemas.GetPhrase])
async def get_phrases(code: Optional[str] = None):
    return await services.phrase_s.filter(code__startswith=code)


@phrases_router.get(
    "/{phrase_id}", response_model=schemas.GetPhrase,
    responses={404: {"model": HTTPNotFoundError}})
async def get_phrase_detail(phrase_id: int):
    return await services.phrase_s.get(id=phrase_id)


@phrases_router.put(
    "/{phrase_id}", response_model=schemas.GetPhrase,
    responses={404: {"model": HTTPNotFoundError}})
async def put_phrase(
        phrase_id: int,
        schema: schemas.UpdatePhrase,
):
    return await services.phrase_s.update(id=phrase_id, schema=schema)
