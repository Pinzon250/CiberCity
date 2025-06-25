from app.database.connection import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nombres = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    correo = Column(String, unique=True, index=True, nullable=False)
    contraseña = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    status = Column(Boolean, default=True)