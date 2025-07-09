from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from starlette.middleware.sessions import SessionMiddleware
import os

# Rutas
from app.routes.pages import catalogo, carrito
from app.routes.auth import users, google
from app.database.connection import Base, engine

load_dotenv()

FRONT_URL = os.getenv("FRONT_URL")

def create_tables():
    Base.metadata.create_all(bind=engine)
create_tables()

app = FastAPI()

# Google session
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SESSION_SECRET_KEY", "super-secret-session"))

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONT_URL, "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Routes
app.include_router(users.router)
app.include_router(google.router)
app.include_router(catalogo.router)
app.include_router(carrito.router)
