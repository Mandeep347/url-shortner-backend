from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import JWTError
from sqlalchemy.orm import Session

from app.core.security import decode_access_token
from app.database.session import get_db
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login",
)

def get_auth_service() -> AuthService:
    return AuthService(UserRepository())

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    payload = decode_access_token(token)

    if payload is None:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail= "Inavlid tokens",
        )

    repository = UserRepository()

    user = repository.get_by_id(
        db,
        int(payload.sub),
    )

    if user is None:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail= "User not found",
        )

    return user