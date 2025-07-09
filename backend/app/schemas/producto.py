from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Importar el schema de categoria
from .categoria import CategoriaOut

class ImagenProductoOut(BaseModel):
    id: int
    imagen: str

    model_config = {
        "from_attributes" : True
    }

class ProductoOut(BaseModel):
    id: int
    nombre: str
    descripcion: Optional[str]
    precio: float
    stock: int
    fecha_creacion: datetime

    categoria: Optional[CategoriaOut]
    imagenes: List[ImagenProductoOut] = []

    model_config = {
        "from_attributes" : True
    }

class ListProducts(BaseModel):
    id: int
    nombre: str
    precio: float
    categoria: Optional[CategoriaOut]
    imagenes: List[ImagenProductoOut]

    model_config = {
        "from_attributes" : True
    }
    
