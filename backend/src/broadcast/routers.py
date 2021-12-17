from asyncio import create_task
from fastapi import APIRouter, Depends, HTTPException, status
from ..users.routers import get_current_superuser
from . import services, schemas


broadcast_router = APIRouter(dependencies=[Depends(get_current_superuser)])


@broadcast_router.post('/', name='Endpoint для рассылки')
async def send_message(schema: schemas.SendMessage):
    create_task(services.send_broadcast(schema))
    return HTTPException(
        status_code=status.HTTP_201_CREATED,
        detail='Рассылка запущена'
    )
