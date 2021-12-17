from tortoise import models, fields


class Phrase(models.Model):
    id = fields.IntField(pk=True)
    code = fields.CharField(max_length=50)
    text = fields.TextField()
