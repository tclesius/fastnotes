from datetime import datetime, timedelta
from jose import jwt
from settings import settings
from user.models import Token


def create_access_token(username: str) -> Token:
    expires_delta = timedelta(minutes=settings.access_token_expire_minutes)
    expires_at = datetime.utcnow() + expires_delta

    token_payload = {
        "sub": username,
        "exp": expires_at,
    }

    access_token = jwt.encode(
        token_payload,
        settings.secret_key,
        algorithm=settings.algorithm,
    )

    return Token(access_token=access_token, token_type="bearer")
