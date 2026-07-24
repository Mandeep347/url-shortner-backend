from sqlalchemy.orm import Session

from app.core.exceptions import (
    EmailAlreadyExistsError,
    InavlidCredentialsError,
    UsernameAlreadyExistsError,
)

from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)

from app.database.models import User
from app.repositories.user_repository import UserRepository
from app.schemas.auth import (
    AccessTokenResponse,
    LoginRequest,
    RegisterRequest,
)

class AuthService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def register(
        self,
        db: Session,
        request: RegisterRequest,
    ) -> User:

        if self.repository.get_by_email(db, request.email):
            raise EmailAlreadyExistsError()

        if self.repository.get_by_username(db, request.username):
            raise UsernameAlreadyExistsError()

        hash_password = hash_password(request.password)

        user = self.repository.create(
            db,
            username=request.username,
            email=request.email,
            hashed_password=hash_password,
        )

        db.commit()
        db.refresh(user)

        return user


    def authenticate_user(
        self,
        db: Session,
        request: LoginRequest,
    ) -> User:

        user = self.repository.get_by_email(
            db,
            request.email,
        )

        if user is None:
            raise InavlidCredentialsError()

        if not verify_password(
            request.password,
            user.hashed_password,
        ):
            raise InavlidCredentialsError()

        return user


    def login(
        self,
        db: Session,
        request: LoginRequest,
    ) -> AccessTokenResponse:

        user = self.authenticate_user(
            db,
            request,
        )

        token = create_access_token(
            subject=str(user.id),
        )

        return AccessTokenResponse(
            access_token=token,
            token_type="bearer",
        )
