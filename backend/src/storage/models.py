from tortoise import models, fields
from ..users.models import UserModel
from ..clients.models import Client


class Category(models.Model):
    id = fields.BigIntField(pk=True)
    name = fields.CharField(max_length=250)


class Product(models.Model):
    id = fields.BigIntField(pk=True)
    title = fields.CharField(max_length=250)
    description = fields.TextField()
    count = fields.IntField(default=None, null=True)
    cost = fields.IntField(default=None, null=True)
    is_deleted = fields.BooleanField(default=False)
    category = fields.ForeignKeyField(
        'models.Category', related_name='products',
        on_delete=fields.CASCADE,
    )
    user = fields.ForeignKeyField(
        'models.UserModel', related_name='products',
        on_delete=fields.CASCADE,
    )


class SoldProduct(models.Model):
    id = fields.BigIntField(pk=True)
    product = fields.ForeignKeyField(
        'models.Product', related_name='sales',
        on_delete=fields.CASCADE
    )
    count = fields.IntField(default=1)


class Sale(models.Model):
    id = fields.BigIntField(pk=True)
    products = fields.ManyToManyField(
        'models.SoldProduct', through="sale_to_products", related_name="sales",
        forward_key='sold_product_id', backward_key='sale_id', default=[]
    )
    client = fields.ForeignKeyField(
        'models.Client', related_name='purchases',
        on_delete=fields.CASCADE, default=None, null=True
    )
