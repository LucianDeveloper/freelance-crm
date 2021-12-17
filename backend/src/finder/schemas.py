from pydantic import BaseModel


class GetResponseProducts(BaseModel):
    pass


class SchemaFilterProducts(BaseModel):
    category_id: int
