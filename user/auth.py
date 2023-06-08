from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from sqlalchemy.orm import Session

from database.core import get_db
from settings import settings
import user.service as user_service


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/signin")


def get_authenticated_user(token: str = Depends(oauth2_scheme), db_session: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        user = user_service.get(db_session=db_session, username=username)
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        return user
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


