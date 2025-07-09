from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth
from starlette.config import Config
from dotenv import load_dotenv
import os

# Db config
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.models.users import User as UserModel

# Auth
from app.routes.auth.auth import create_access_token, hash_password

load_dotenv()

router = APIRouter(
    prefix="/auth",
    tags=["Google Auth"]
)
config = Config(".env")

oauth = OAuth(config)
oauth.register(
    name="google",
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"}
)

@router.get("/google")
async def login_via_google(request: Request):
    redirect_uri= "http://localhost:8000/auth/google/callback"
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/google/callback")
async def google_callback(request: Request, db: Session = Depends(get_db)):
    token = await oauth.google.authorize_access_token(request)
    resp = await oauth.google.get("https://openidconnect.googleapis.com/v1/userinfo", token=token)
    user_info = resp.json()

    correo = user_info.get("email")
    nombres = user_info.get("given_name", "")
    apellidos = user_info.get("family_name", "")

    if not correo:
        return {"error": "No se pudo obtener el cooreo de Google"}
    
    user = db.query(UserModel).filter(UserModel.correo == correo).first()

    if not user:
        user = UserModel(
            nombres= nombres,
            apellidos= apellidos,
            correo=correo,
            contraseña=hash_password("GOOGLE_AUTH" + correo)
        )
        db.add(user)
        db.commit()
        db.refresh(user)

    jwt_token = create_access_token(data={"sub": user.correo, "name": user.nombres})

    redirect_url = (
        f"http://localhost:3000/auth/callback"
        f"?token={jwt_token}"
        f"&nombre={user.nombres}"
        f"&correo={user.correo}"
    )
    print("USER INFO:", user_info)
    return RedirectResponse(url = redirect_url)