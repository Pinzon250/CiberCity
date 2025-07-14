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

class PromocionCreate(BaseModel):
    titulo: str
    descripcion: str
    descuento_procentaje: str
    fecha_inicio: datetime
    fecha_fin: datetime
    producto_ids: Optional[List[int]] = []
    categoria_ids: Optional[List[int]] = []
    
class PromocionOut(BaseModel):
    id: int
    titulo: str
    descripcion: str
    descuento_porcentaje: float
    fecha_inicio: datetime
    fecha_fin: datetime
    activa: bool

    model_config = {
        "from_attributes": True
    }
