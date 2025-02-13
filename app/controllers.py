from fastapi import APIRouter, Depends
from sqlmodel import Session
from .database import get_session
from .models import User
from .repositories import create_user, get_users, get_user_by_id

router = APIRouter()

@router.post("/users/", response_model=User)
def add_user(user: User, session: Session = Depends(get_session)):
    return create_user(session, user)

@router.get("/users/", response_model=list[User])
def list_users(session: Session = Depends(get_session)):
    return get_users(session)

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, session: Session = Depends(get_session)):
    user = get_user_by_id(session, user_id)
    if not user:
        return {"error": "User not found"}
    return user
