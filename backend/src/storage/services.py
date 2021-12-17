from re import sub
from uuid import uuid4
from fastapi import HTTPException, status
from src.base.services import BaseService
from . import models, schemas
from datetime import datetime, timedelta


class CategoryService(BaseService):
    model = models.Category
    create_schema = schemas.CreateCategory
    update_schema = schemas.CreateCategory
    get_schema = schemas.GetCategory
    get_detail = schemas.GetCategory


class ProductService(BaseService):
    model = models.Product
    create_schema = schemas.CreateProduct
    update_schema = schemas.CreateProduct
    get_schema = schemas.GetProduct
    get_detail = schemas.GetProduct


class SaleService(BaseService):
    model = models.Sale
    create_schema = schemas.CreateSale
    update_schema = schemas.CreateSale
    get_schema = schemas.GetSale
    get_detail = schemas.GetSale


category_s = CategoryService()
product_s = ProductService()
sale_s = SaleService()
