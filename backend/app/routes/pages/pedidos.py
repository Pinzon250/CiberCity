from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.routes.auth.auth import get_current_user

from app.models import User, Pedido, PedidoItem, Valoraciones
from app.schemas.carrito import PedidoOut
from app.schemas.users import ValoracionCreate, ValoracionOut

from typing import List

router = APIRouter(
    prefix="/pedidos",
    tags=["Pedidos y valoraciones"]
)


# ----------------------- ENDPOINTS DE PEDIDOS ----------------------- #
# Obtener pedido actual
@router.get("/pedido-actual", response_model=PedidoOut)
def obtener_pedido_actual(
    usuario: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    pedido = (db.query(Pedido).filter(
        Pedido.usuario_id == usuario.id,
        Pedido.estado.in_(["procesando","enviando"])
        )
        .order_by(Pedido.fecha_pedido.desc())
        .first()
    )
    if not pedido:
        raise HTTPException(status_code=404, detail="No tienes pedidos activos")
    
    return pedido

# Obtener historial de pedidos
@router.get("/historial-pedidos", response_model=List[PedidoOut])
def obtener_historial_pedidos(
    db: Session = Depends(get_db),
    usuario: User = Depends(get_current_user)
):
    pedidos = (db.query(Pedido).filter(Pedido.usuario_id == usuario.id, Pedido.estado == "entregado").order_by(Pedido.fecha_pedido.desc()).all())
    
    return pedidos

# Agregar en produccion obtener Guia del envio
@router.get("/guia")
def obtener_guia_envio(usuario: User = Depends(get_current_user)):
    return { "Guia"}

# ------------------------------ ENDPOINT DE VAOLARACIONES --------------------------
@router.post("/valoraciones", response_model=ValoracionOut)
def crear_valoracion(
    data: ValoracionCreate,
    db: Session = Depends(get_db),
    usuario: User = Depends(get_current_user)
):
    compro = db.query(PedidoItem).join(PedidoItem.pedido).filter(
        PedidoItem.producto_id == data.producto_id,
        PedidoItem.pedido.has(usuario_id = usuario.id)
    ).first()

    if not compro:
        raise HTTPException(status_code=403, detail="Sollo puedes valorar productos que compraste")
    
    ya_valoro = db.query(Valoraciones).filter_by(usuario_id = usuario.id, producto_id = data.producto_id).first()

    if ya_valoro:
        raise HTTPException(status_code=400, detail="Ya valoraste este producto")
    
    nueva = Valoraciones(
        usuario_id = usuario.id,
        producto_id = data.producto_id,
        estrellas = data.estrellas,
        comentario = data.comentario,
        imagen_url = data.imagen_url
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    return nueva
