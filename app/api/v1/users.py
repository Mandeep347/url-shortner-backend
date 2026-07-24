from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

service = UserService()

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return service.create_user(
        db,
        user
    )


@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return service.get_user(db)

@router.get("/{id}", response_model=UserResponse)
def get_user_by_id(id: int, db:Session = Depends(get_db)):
    return service.get_user_by_id(db, id)

@router.put("/{id}", response_model=UserResponse)
def update_user(id: int, user: UserCreate, db: Session = Depends(get_db)):
    return service.update_user(db, id, user)

@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    return service.delete_user(db, id)