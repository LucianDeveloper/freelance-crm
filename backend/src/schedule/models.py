from tortoise import models, fields


class Schedule(models.Model):
    id = fields.BigIntField(pk=True)
    time_start = fields.DatetimeField()
    time_end = fields.DatetimeField()
    description = fields.TextField()
