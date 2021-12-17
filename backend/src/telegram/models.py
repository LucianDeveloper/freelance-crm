from tortoise import models, fields


class TGUser(models.Model):
    id = fields.BigIntField(pk=True)
    username = fields.CharField(max_length=250, default=None, null=True)
    first_name = fields.CharField(max_length=250, default=None, null=True)
    last_name = fields.CharField(max_length=250, default=None, null=True)
    join_date = fields.DatetimeField(auto_now_add=True)
    phone = fields.CharField(max_length=15, default=None, null=True)
