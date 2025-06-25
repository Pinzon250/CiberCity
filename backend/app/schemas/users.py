from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# User Model (Class)

# Schema of User
class User(BaseModel):
    id: int
    nombres: str
    correo: str
    contraseña: str
    created_at: datetime = datetime.now()

    model_config = {
        "from_attributes": True
    }

# schema of User Registration
class UserCreate(BaseModel):
    nombres: str
    apellidos: str
    correo: EmailStr
    contraseña: str

# Schema of User Login
class UserLogin(BaseModel):
    correo: str
    contraseña: str   