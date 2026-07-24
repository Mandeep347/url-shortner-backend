from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models import User

class UserRepository:

    def create(
            self,
            db: Session,
            *,
            username: str,
            email: str,
            hashed_password: str,
    ) -> User:
        
        user = User(
            username = username,
            email = email,
            hashed_password= hashed_password
        )

        db.add(user)

        return user

    def get_by_email(self, db: Session, email: str) -> User | None:
        statement = select(User).where(
            User.email == email
        )
        return db.scalar(statement)

    def get_by_username(self, db: Session, username: str) -> User | None:
        statement = select(User).where(
            User.username == username
        )
        return db.scalar(statement)

    def get_by_id(self, db: Session, user_id: int) -> User | None:
        return db.get(
            User,
            user_id,
        )