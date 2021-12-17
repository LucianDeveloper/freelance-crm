from fastapi import APIRouter, Depends

from src.users.routers import get_current_active_user
from src.telegram.endpoints.tgusers import tg_user_router

persons_router = APIRouter(dependencies=[Depends(get_current_active_user)])


persons_router.include_router(tg_user_router, prefix='/tg')
