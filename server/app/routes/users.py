from fastapi import APIRouter

from app.models.user import UserCreate
from app.services.auth import hash_password
from app.database import db

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def create_user(user: UserCreate):
    hashed_password = hash_password(user.password)

    user_document = {
        "username": user.username,
        "email": user.email,
        "password_hash": hashed_password
    }

    result = db.users.insert_one(user_document)

    return {
        "message": "User created successfully",
        "user_id": str(result.inserted_id),
        "username": user.username,
        "email": user.email
    }