from pwdlib import PasswordHash
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt

from app.core.config import settings
from app.schemas.auth import TokenPayload

password_hash = PasswordHash.recommended()

def hash_password(password: str) -> str:
    return password_hash.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)

def create_access_token(subject: int):

    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)

    payload = {
        "sub": subject,
        "exp": expire
    }

    return jwt.encode(
        payload,
        settings.secret_key,
        algorithm=settings.algorithm,
    )

def decode_access_token(token: str) -> TokenPayload | None:
    try:
        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[settings.algorithm],
        )

        return TokenPayload(**payload)
    
    except JWTError:
        return None