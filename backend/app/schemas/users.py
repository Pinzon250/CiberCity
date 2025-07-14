from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

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
    correo: EmailStr
    contraseña: str   

class UserOut(BaseModel):
    nombres: str
    apellidos: str
    correo: EmailStr

    model_config = {
        "from_attributes": True
    }

class UserUpdate(BaseModel):
    nombres: str
    apellidos: str
    correo: EmailStr

    model_config = {
        "from_attributes": True
    }

class ForgotPasswordRequest(BaseModel):
    correo: EmailStr

class ResetPasswordRequest(BaseModel):
    token: str
    nueva_contraseña: str

# Direcciones 
class DireccionesEnvio(BaseModel):
    direccion: str
    ciudad: str
    departamento: str
    pais: str
    codigo_postal: str
    telefono: str
    
# Metodos de pago
class MetodoPago(BaseModel):
    alias: Optional[str] = None
    tipo: str
    detalles: str

# Lista de deseos
class WhislistIn(BaseModel):
    producto_id: int

# Valoraciones
class ValoracionCreate(BaseModel):
    producto_id: int
    estrellas: int  = Field(ge=1, le=5)
    comentario: str
    imagen_url: Optional[str] = None

class ValoracionOut(BaseModel):
    id: int
    producto_id: int
    estrellas: int
    comentario: str
    imagen_url: Optional[str]
    fecha: datetime

    model_config = {
        "from_attributes": True
    }

class MensajeContactoCreate(BaseModel):
    asunto: str
    mensaje: str

class MensajeContactoOut(BaseModel):
    id: int
    asunto: str
    mensaje: str
    fecha: datetime

    model_config = {
        "from_attributes": True
    }

class FAQOut(BaseModel):
    id: int
    pregunta: str
    respuesta: str
    
    model_config = {
        "from_attributes": True
    }