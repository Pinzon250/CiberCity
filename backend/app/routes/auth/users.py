from fastapi import APIRouter, Depends, HTTPException
from app.models.users import User as UserModel
from app.schemas.users import UserLogin, UserCreate, ForgotPasswordRequest, ResetPasswordRequest
from app.database.connection import get_db
from sqlalchemy.orm import Session
from app.models import users
from passlib.context import CryptContext
from app.routes.auth.auth import create_access_token, verify_password, hash_password

from datetime import timedelta
from jose import jwt, JWTError
from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from dotenv import load_dotenv
import os

load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

FRONT_URL=os.getenv("FRONT_URL")
SECRET_KEY = os.getenv("AUTH_SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

#Mail Config
conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,     
    USE_CREDENTIALS=True,
)

router = APIRouter(
    prefix="/user",
    tags=["Auth users"]   
)

# Create a new user
@router.post("/register")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Verificando que el correo no exista
    existing_user = db.query(users.User).filter(users.User.correo == user.correo).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Correo ya registrado")
    
    # Create a new user
    new_user = UserModel (
        nombres=user.nombres,
        apellidos=user.apellidos,
        correo=user.correo,
        contraseña=hash_password(user.contraseña)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully"}

# Login user
@router.post("/login")
def login_user(user_login: UserLogin, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.correo == user_login.correo).first()

    if not user or not verify_password(user_login.contraseña, user.contraseña):
        raise HTTPException(
            status_code=404,
            detail="Credenciales invalidas"
        )
    
    token = create_access_token(data={"sub": user.correo, "name": user.nombres})

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "correo": user.correo,
            "nombres": user.nombres,
        }
    }

@router.post("/forgot-password")
async def forgot_password(data: ForgotPasswordRequest, background_task: BackgroundTasks, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.correo == data.correo).first()
    if not user:
        raise HTTPException(status_code=404, detail="Correo no encontrado")
    
    # Create temp token for reset
    token = create_access_token(data={"sub": user.correo}, expires_delta=timedelta(minutes=15))

    # URL to frontend
    reset_link = f"{FRONT_URL}auth/reset-password?token={token}"

    message = MessageSchema(
        subject="Recuperar contraseña - CiberCity",
        recipients = [data.correo],
        body= f"Hola {user.nombres}, \n\nUsa el siguiente enlace para reestablecer tu contraseña: {reset_link} \n\nEste enlace expirara en 15 minutos.",
        subtype= "plain"
    )

    fm = FastMail(conf)
    background_task.add_task(fm.send_message, message)

    return {"msg": "Correo enviado para recuperar contraseña"}

@router.post("/reset-password")
def reset_password(data: ResetPasswordRequest, db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(data.token, SECRET_KEY, algorithms=[ALGORITHM])
        correo = payload.get("sub")
        if correo is None:
            raise HTTPException(status_code = 400, detail = "Token invalido")
        
    except JWTError:
        raise HTTPException(status_code = 400, detail = "Token invalido o expirado")
    
    user = db.query(UserModel).filter(UserModel.correo == correo).first()
    if not user:
        raise HTTPException(status_code=404, detail= "Usuario no encontrado")
    
    user.contraseña = hash_password(data.nueva_contraseña)
    db.commit()

    return {"msg": "Contraseña restablecida correctamente"}
