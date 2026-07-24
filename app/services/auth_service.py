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