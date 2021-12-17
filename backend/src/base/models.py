from tortoise import models, fields


class File(models.Model):
    id = fields.BigIntField(pk=True)
    url = fields.CharField(max_length=255)
    size = fields.BigIntField(default=None, null=True, description='kb')
