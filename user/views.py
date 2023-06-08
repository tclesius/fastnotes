from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database.core import get_db
from user.auth import get_authenticated_user
from user.jwt import create_access_token
from user.models import User, UserCreate, UserRead
from user.hashing import verify_password, create_password_hash
import user.service as user_service

router = APIRouter()


@router.post("/signup", response_model=UserRead)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = user_service.get(db_session=db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    db_user = user_service.get(db_session=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = create_password_hash(user.password)
    db_user = user_service.create(db_session=db, user_in=UserCreate(username=user.username, email=user.email,
                                                                    password=hashed_password))
    return db_user


@router.post("/signin")
def signin(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = user_service.get(db_session=db, username=form_data.username)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token = create_access_token(user.username)
    return access_token


# Usage example
@router.get("/me", response_model=UserRead)
def get_current_user(current_user: User = Depends(get_authenticated_user)):
    return current_user
