from tortoise import models, fields


class BroadcastHistory(models.Model):
    id = fields.BigIntField(pk=True)
    send_date = fields.DatetimeField(auto_now_add=True)
    count_all = fields.IntField()
    count_success = fields.IntField()
    text = fields.TextField()
