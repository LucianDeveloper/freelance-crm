from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI, APIRouter, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from src.users.routers import (
    fastapi_cookies, cookie_authentication,
    get_current_superuser
)
from src.users.routers import users_router
from src.telegram.routers import persons_router
from src.notifications.routers import notify_router
from src.broadcast.routers import broadcast_router
from src.languages.routers import languages_router
from src.storage.routers import storage_router

from src.finder.routers import finder_router

from src.languages.on_startup import init_russian_phrases

from scripts import create_superuser

from config import DB_URL, db_paths
from config import ALLOW_CORS


app = FastAPI(
    title="FreelanceCRM",
    version="0.0.1",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOW_CORS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

api = APIRouter(prefix="/api",)

api.include_router(
    fastapi_cookies.get_auth_router(cookie_authentication), prefix="/auth/jwt", tags=["Auth"]
)
api.include_router(
    fastapi_cookies.get_register_router(), prefix="/auth", tags=["Auth"],
    dependencies=[Depends(get_current_superuser)]
)

api.include_router(users_router, prefix="/users", tags=["Users"])
api.include_router(languages_router, prefix="/langs", tags=["Languages"])
api.include_router(persons_router, prefix="/persons", tags=["Telegram users"])
api.include_router(notify_router, prefix="/notify", tags=["Notifications"])
api.include_router(broadcast_router, prefix="/broadcast", tags=["Broadcast"])
api.include_router(storage_router, prefix="/storage", tags=["Storage"])
api.include_router(finder_router, prefix='/finder', tags=['Finder'])

app.mount("/api/media", StaticFiles(directory="media"), name="media")


app.include_router(api)

register_tortoise(
    app,
    db_url=DB_URL,
    modules={"models": db_paths.all_paths},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.on_event('startup')
async def on_startup():
    """This function exec on start up"""
    await create_superuser.main(True)
    await init_russian_phrases()
