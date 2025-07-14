from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db

from app.models import User, Producto, Pedido, DireccionEnvio, ListaDeseos
from app.schemas.users import UserOut, UserUpdate, DireccionesEnvio, MetodoPago
from app.schemas.producto import ProductoOut
from app.schemas.carrito import PedidoOut
from app.routes.auth.auth import get_current_user

from typing import List


router = APIRouter(
    prefix="/perfil",
    tags=["Perfil de usuarios"]
)


# ----------------------- ENDPOINTS DE USUARIOS ----------------------- #
# Obtener los datos del usuario
@router.get("/", response_model=UserOut)
def obtener_perfil(
    usuario: User = Depends(get_current_user),
    db: Session = Depends(get_db)):
    return usuario

# Actualizar datos del usuario
@router.put("/actualizar-perfil",  response_model=UserUpdate)
def actualizar_perfil(
    data: UserUpdate,
    usuario_actual: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):  
    usuario = db.query(User).filter_by(id = usuario_actual.id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    usuario.nombres = data.nombres,
    usuario.apellidos= data.apellidos,
    usuario.correo = data.correo,

    db.commit()
    db.refresh(usuario)

    return usuario

# --------------------------- ENDPOINTS DE DIRECCIONES --------------------------- #
@router.post("/direcciones", response_model=DireccionesEnvio)
def agregar_direcciones(
    data: DireccionesEnvio,
    usuario: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    nueva = DireccionEnvio(
        usuario_id=usuario.id,
        **data.dict()
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    return nueva
    
# Eliminar direccion
@router.delete("/direccion/{direccion_id}")
def eliminar_direccion(
    direccion_id: int, 
    usuario : User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    direccion = db.query(DireccionEnvio).filter_by(id= direccion_id, usuario_id=usuario.id).first()
    if not direccion:
        raise HTTPException(status_code=404, detail="Direccion no encontrada")
    
    db.delete(direccion)
    db.commit()
    return {
        "msg": "Direccion eliminada correctamente"
    }

# --------------------------- ENDPOINTS DE METODOS DE PAGO --------------------------- #
# Refactorizar cuando este en produccion
@router.post("/metodo_pago", response_model=MetodoPago)
def agregar_metodo_pago(
    data: MetodoPago,
    usuario: User = Depends(get_current_user),  
    db: Session = Depends(get_db)
):
    metodo = MetodoPago(
        usuario_id=usuario.id,
        **data.dict()
    )
    db.add(metodo)
    db.commit()
    db.refresh(metodo)

    return {
        "msg": "Metodo de pago agregado correctamente"
    }


# --------------------------------- ENDPOINTS DE LISTAS DESEOS --------------------------- #
@router.post("/agregar/{producto_id}")
def agregar_a_deseados(
    producto_id: int, 
    db: Session = Depends(get_db), 
    usuario: User = Depends(get_current_user)
):
    producto = db.query(Producto).filter_by(id = producto_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    ya_existe = db.query(ListaDeseos).filter_by(usuario_id = usuario.id, producto_id = producto.id).first()
    
    if ya_existe:
        raise HTTPException(status_code=400, detail="Este producto ya esta en tu lista de deseos")
    
    nuevo = ListaDeseos(usuario_id = usuario.id, producto_id = producto.id)
    db.add(nuevo)
    db.commit()
    return { "msg":"Producto agregado a la lista de deseos"}

@router.delete("/eliminar/{producto_id}")
def eliminar_de_deseados(
    producto_id: int, 
    db: Session = Depends(get_db), 
    usuario: User = Depends(get_current_user)
):
    producto = db.query(ListaDeseos).filter_by(usuario_id = usuario.id, producto_id = producto_id).first()

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no esta en la lista de deseados")
    
    db.delete(producto)
    db.commit()


    return { "msg": "Removido de la lista de deseos"}

@router.get("/productos-deseados", response_model=List[ProductoOut])
def listar_deseados(
    db: Session = Depends(get_db), 
    usuario: User = Depends(get_current_user)
):
    relaciones = db.query(ListaDeseos).filter_by(usuario_id = usuario.id).all()
    productos = [rel.producto for rel in relaciones]

    return productos
