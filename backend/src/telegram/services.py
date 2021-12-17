from re import sub
from uuid import uuid4
from fastapi import HTTPException, status
from src.base.services import BaseService
from src.telegram import models, schemas
from datetime import datetime, timedelta


class TGUserService(BaseService):
    model = models.TGUser
    create_schema = schemas.CreateTGUser
    update_schema = schemas.UpdateTGUser
    get_schema = schemas.GetTGUser
    get_detail = schemas.GetTGUser

    def __init__(self):
        self.codes = {}

    async def add_code(self, phone):
        clear_phone = sub(r'[^\d]', '', phone)
        self.codes.update({
            clear_phone: (str(uuid4().hex)[:4], datetime.now())
        })

    async def get_code(self, schema: schemas.SchemaPhone):
        try:
            phone = sub(r'[^\d]', '', schema.phone)
            code, time = self.codes[phone]
            if time + timedelta(minutes=5) > datetime.now():
                return schemas.GetCode(code=code)
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail='Время действия истекло'
            )
        except:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Активный код не найден'
            )


tg_user_s = TGUserService()
