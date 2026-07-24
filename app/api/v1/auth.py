from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_auth_service, get_current_user
from app.core.exceptions import (
    EmailAlreadyExistsError,
    InavlidCredentialsError,
    UsernameAlreadyExistsError,
)

from app.database.session import get_db
from app.database.models import User
from app.schemas.auth import (
    AccessTokenResponse,
    LoginRequest,
    RegisterRequest,
)

from app.schemas.user import UserResponse
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db),
    service: AuthService = Depends(get_auth_service),
):

    try:
        return service.register(db, request)

    except EmailAlreadyExistsError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists",
        )

    except UsernameAlreadyExistsError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already exists",
        )

@router.post(
    "/login",
    response_model=AccessTokenResponse,
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db),
    service: AuthService = Depends(get_auth_service),
):

    try:
        service.login(db, request)

    except InavlidCredentialsError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

@router.get(
    "/me",
    response_model= UserResponse,
)
def get_me(
    current_user: User = Depends(get_current_user),
):
    return current_user