from sqlalchemy.sql.functions import user
from fastapi import HTTPException, APIRouter, Request, Depends, status, Header
from typing import Optional
from fastapi.security import OAuth2PasswordBearer
from auth.controller import AuthController
from macapa import controller as macapa_controller
from varejao import controller as varejao_controller
from pydantic import BaseModel
from jose import JWTError


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

auth_controller = AuthController()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Login(BaseModel):
    client: str
    email: str
    password: str


@router.post("/")
async def login(login: Login):
    
    if login.client == "macapa":
        user_controller = macapa_controller
    elif login.client == "varejao":
        user_controller = varejao_controller
    else:
        return {'detail': 'This client does not exist'}
    
    try:
        user = auth_controller.authenticate_user(login, user_controller)
    except Exception as e:
        return {'detail': str(e)}

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha incorreto",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = auth_controller.generate_token({'id': str(user.id), 'email': str(user.email), 'client': str(login.client)})
    return {"access_token": access_token, "token_type": "bearer"}

async def verify_token(request: Request, token: str = Depends(oauth2_scheme)):
    try:
        user = auth_controller.verify_token(token)
        client_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Not authorized',
            headers={"WWW-Authenticate": "Bearer"},
        )
        if user:
            if str(user['client']) in str(request['path']):
                return user
            else: 
                raise client_exception
        else:
            raise client_exception
    except JWTError as e:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )
        raise credentials_exception