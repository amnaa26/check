from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
import os

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

def create_access_token(data: dict, expires=60):
    to_encode = data.copy()
    # Use timezone-aware datetime
    to_encode.update({"exp": datetime.now(timezone.utc) + timedelta(minutes=expires)})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        return None
