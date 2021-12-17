from tortoise import models, fields


class NotificationHistory(models.Model):
    id = fields.BigIntField(pk=True)
    send_date = fields.DatetimeField(auto_now_add=True)
    status = fields.SmallIntField()
