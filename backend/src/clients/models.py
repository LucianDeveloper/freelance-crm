from tortoise import models, fields
from ..telegram.models import TGUser


class Client(models.Model):
    id = fields.BigIntField(pk=True)
    fio = fields.CharField(max_length=250)
    phone = fields.CharField(max_length=25)
    url_tg = fields.CharField(max_length=250, default=None, null=True)
    url_inst = fields.CharField(max_length=250, default=None, null=True)
    tg_user = fields.OneToOneField(
        'models.TGUser', related_name='client',
        on_delete=fields.CASCADE, default=None, null=True
    )
