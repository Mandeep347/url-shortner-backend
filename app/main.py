from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database.models import User

from app.database.session import get_db
from app.api.v1.users import router as users_router
from app.api.v1.auth import router as auth_router
from app.core.config import Settings

app = FastAPI(
    title=Settings.app_name,
    version=Settings.app_version,
)

app.include_router(users_router, prefix="/api/v1")
app.include_router(auth_router, prefix="/api/v1")
