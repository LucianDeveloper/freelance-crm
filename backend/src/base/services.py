from typing import TypeVar, Type, Optional, List
from fastapi import HTTPException
from pydantic import BaseModel
from tortoise import models
from abc import ABC


ModelType = TypeVar("ModelType", bound=models.Model)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
GetSchemaType = TypeVar("GetSchemaType", bound=BaseModel)
QuerySchemaType = TypeVar("QuerySchemaType", bound=BaseModel)


class BaseService(ABC):
    model: Type[ModelType]
    create_schema: CreateSchemaType
    update_schema: UpdateSchemaType
    query_schema: QuerySchemaType
    get_schema: GetSchemaType
    get_detail: GetSchemaType

    async def create(self, schema, **kwargs) -> Optional[GetSchemaType]:
        obj = await self.model.create(**schema.dict(exclude_unset=True), **kwargs)
        return await self.get(pk=obj.pk)

    async def get_or_create(self, schema, **kwargs) -> Optional[GetSchemaType]:
        obj, _ = await self.model.get_or_create(**schema.dict(exclude_unset=True), **kwargs)
        return await self.get(pk=obj.pk)

    async def update(self, schema, exclude=None, **kwargs) -> Optional[GetSchemaType]:
        if exclude is not None:
            new_dict = {}
            s_dict = schema.dict()
            for key in s_dict.keys():
                if key not in exclude:
                    new_dict.update({key: s_dict[key]})
            await self.model.filter(**kwargs).update(**new_dict)
        else:
            await self.model.filter(**kwargs).update(**schema.dict(exclude_unset=True))
        return await self.get(**kwargs)

    async def delete(self, **kwargs):
        obj = await self.model.filter(**kwargs).delete()
        if not obj:
            raise HTTPException(status_code=404, detail='Запись не существует!')

    async def all(self) -> Optional[GetSchemaType]:
        return [await self.get(id=pk) for pk in await self.model.all().values_list('id', flat=True)]

    async def filter(
            self, limit=None, offset=None,
            order_by: Optional[List[str]] = None,
            **kwargs
    ) -> Optional[GetSchemaType]:
        query = self.model.filter(**{x: y for x, y in kwargs.items() if y is not None})
        if offset:
            query = query.offset(offset)
        if limit:
            query = query.limit(limit)
        if order_by:
            query = query.order_by(*order_by)
        records_ids = await query.order_by('id').values_list('id', flat=True)
        return [await self.get(id=pk) for pk in records_ids]

    async def get(self, **kwargs) -> Optional[GetSchemaType]:
        return await self.get_detail.from_queryset_single(self.model.get(**kwargs))

    async def get_obj(self, **kwargs) -> Optional[ModelType]:
        return await self.model.get_or_none(**kwargs)
