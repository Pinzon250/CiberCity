from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from decimal import Decimal
from datetime import datetime

from .producto import ProductoOut


class CarritoItemOut(BaseModel):
    id: int
    cantidad: int
    producto: ProductoOut

    model_config = {
        "from_attributes": True
    }

class CarritoOut(BaseModel):
    id: int
    usuario_id: int
    cupon_codigo: Optional[str] = None
    items: List[CarritoItemOut]

    model_config = ConfigDict(from_attributes=True)

class CarritoAgregarIn(BaseModel):
    producto_id: int
    cantidad: int

class AplicarCuponIn(BaseModel):
    codigo: str

class SimularPagoIn(BaseModel):
    metodo_pago: str

# Pedidos
class PedidoItemOut(BaseModel):
    id: int
    producto: ProductoOut
    cantidad: int
    precio_unitario: Decimal

    model_config = {
        "from_attributes": True
    }

class PedidoOut(BaseModel):
    id: int
    usuario_id: int
    total: Decimal
    pagado: bool
    fecha_pedido: datetime
    estado: Optional[str] = None
    numero_guia: Optional[str] = None  
    items: List[PedidoItemOut]

    model_config = {
        "from_attributes": True
    }

class ActualizarCantidadIn(BaseModel):
    producto_id: int
    cantidad: int