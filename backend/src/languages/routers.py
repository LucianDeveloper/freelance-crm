from fastapi import APIRouter, Depends

from src.users.routers import get_current_active_user
from src.languages.endpoints.phrases import phrases_router

languages_router = APIRouter(dependencies=[Depends(get_current_active_user)], tags=['Languages'])

languages_router.include_router(phrases_router, prefix='/phrases')
