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
@router.get("/", response_model=dict)
def obtener_carrito(usuario_id: int, db: Session = Depends(get_db)):
    carrito = db.query(Carrito).filter_by(usuario_id = usuario_id).first()
    if not carrito:
        raise HTTPException(status_code=404, detail="Carrito no encontrado")
    
    total = sum(item.producto.precio * item.cantidad for item in carrito.items)

    # Aplicar cupon si hay
    if carrito.cupon_codigo:
        cupon = db.query(Cupon).filter_by(codigo=carrito.cupon_codigo).first()
        if cupon and cupon.activo:
            descuento = total * (cupon.descuento / 100)
            total -= descuento

    return {
        "carrito": carrito,
        "total": float(total)
    }

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

# Quitar producto
@router.delete("/eliminar/{item_id}")
def eliminar_item_carrito(item_id:int, usuario_id: int, db: Session = Depends(get_db)):
    item = db.query(CarritoItem).join(Carrito).filter(
        CarritoItem.id == item_id,
        Carrito.usuario_id == usuario_id
    ).first()

    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    
    db.delete(item)
    db.commit()
    return {"msg":"Item eliminado del carrito"}

# Aplicar cupones
@router.post("/cupon")
def aplicar_cupon(data: AplicarCuponIn, usuario_id: int, db: Session = Depends(get_db)):
    cupon = db.query(Cupon).filter_by(codigo=data.codigo).first()

    if not cupon or not cupon.activo:
        raise HTTPException(status_code=400, detail="Cupon invalido o inactivo")
    
    if cupon.fecha_expiracion and cupon.fecha_expiracion < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Cupon expirado")
    
    usos_usuario = db.query(CuponUso).filter_by(usuario_id = usuario_id, cupon_id = cupon.id).count()
    if usos_usuario >= cupon.max_usos_por_usuario:
        raise HTTPException(status_code=400, detail="Limite de uso alcanzado para este cupon")
    
    carrito = db.query(Carrito).filter_by(usuario_id=usuario_id).first()
    if not carrito:
        raise HTTPException(status_code=404, detail="Carrito no encontrado")
    
    carrito.cupon_codigo = data.codigo
    db.commit()

    total = sum(item.producto.precio * item.cantidad for item in carrito.items)
    descuento = total * (cupon.descuento / 100)
    total -= descuento

    return {
        "msg": "Cupon aplicado correctamente",
        "total_con_descuento": float(total)
    }
