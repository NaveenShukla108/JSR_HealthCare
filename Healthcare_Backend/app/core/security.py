from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

from uuid import UUID

SECRET_KEY = "django-insecure-_t^oe9b-ezm%!ry&c(3s)h))bcd0p+fq%#a+3b5@1_cxgf_wd1"
ALGORITHM = "HS256"

security = HTTPBearer()


class CurrentUser:
    def __init__(self, user_id: UUID, role: str):
        self.id = user_id
        self.role = role

    

def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(security),
) -> CurrentUser:
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid Token")
    
    user_id = payload.get("user_id")
    role = payload.get("role")

    if not user_id or not role:
        raise HTTPException(status_code=401, detail="Invalid payload, UserID or role not found!")
    
    return CurrentUser(user_id=UUID(user_id), role=role)

    