from fastapi_users.db import TortoiseBaseUserModel
from tortoise import fields
# from ..telegram.models import TGUser


class UserModel(TortoiseBaseUserModel):
    first_name = fields.CharField(null=False, max_length=255)
    last_name = fields.CharField(null=False, max_length=255)
    patronymic_name = fields.CharField(max_length=255, null=True, default=None)
    is_verified = fields.BooleanField(default=True, null=False)
    inn = fields.CharField(max_length=20)
