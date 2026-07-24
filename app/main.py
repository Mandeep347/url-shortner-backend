from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database.models import User

from app.database.session import get_db
from app.api.v1.users import router as users_router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.include_router(users_router, prefix="/api/v1")

