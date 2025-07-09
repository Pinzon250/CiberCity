from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models import Carrito, CarritoItem, Pedido
from app.models.carrito import Cupon, CuponUso, PedidoItem
from app.schemas.carrito import CarritoAgregarIn, AplicarCuponIn, SimularPagoIn, CarritoOut

from datetime import datetime
from decimal import Decimal

router = APIRouter(
    prefix="/Carrito",
    tags=["Carrito"]
)

# Ver el carrito actual
@router.get("/", response_model=CarritoOut)
def obtener_carrito(usuario_id: int, db: Session = Depends(get_db)):
    carrito = db.query(Carrito).filter_by(usuario_id = usuario_id).first()
    if not carrito:
        raise HTTPException(status_code=404, detail="Carrito no encontrado")
    return carrito

# Agregar producto
@router.post("/agregar")
def agregar_producto(data:CarritoAgregarIn, usuario_id: int, db: Session = Depends(get_db)):
    carrito = db.query(Carrito).filter_by(usuario_id = usuario_id).first()
    if not carrito:
        carrito = Carrito(usuario_id = usuario_id)
        db.add(carrito)
        db.commit()
        db.refresh(carrito)

    item = next((i for i in carrito.items if i.producto_id == data.producto_id), None)
    if item:
        item.cantidad += data.cantidad
    else: 
        nuevo_item = CarritoItem(
            carrito_id=carrito.id,
            producto_id=data.producto_id,
            cantidad=data.cantidad
        )
        db.add(nuevo_item)

    db.commit()
    return {"msg" : "Producto agregado al carrito"}
