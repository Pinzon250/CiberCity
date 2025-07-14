# Importar FastAPI
from fastapi import APIRouter, Depends, Query, HTTPException

# Sesiones con la base de datos
from sqlalchemy.orm import Session

# Tipos de datos
from typing import Optional, List
from decimal import Decimal

# Importar schemas, base de datos
from app.database.connection import get_db
from app.models.producto import Producto
from app.models.categoria import Categoria
from app.schemas.producto import ProductoOut, ListProducts
from app.schemas.users import ValoracionOut
from app.models.users import Valoraciones


# Tag y Ruta inicial
router = APIRouter(
    prefix="/catalogo",
    tags=["Catalogo"]
)

# Endpoint para obtener todos los productos
@router.get("/productos", response_model=List[ListProducts])
# Crear funcion con los parametros de filstros de: Categoria, precio minimo y maximo, marca, busquedas y limites de productos obtenidos
def listar_productos(
    db: Session = Depends(get_db),
    categoria_nombre: Optional[str] = Query(None),
    precio_min: Optional[float] = Query(None),
    precio_max: Optional[float] = Query(None),
    # Agregar Marca
    marca: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    skip: int = 0,
    limit: int = 20
):
    # Obtener los productos
    query = db.query(Producto)

    # Filtrar por categoria
    if categoria_nombre:
        query = query.join(Producto.categoria).filter(Categoria.nombre.ilike(f"%{categoria_nombre}%"))

    # Filtrar por precio minimo
    if precio_min is not None:
        print("precio_min:", precio_min)
        query = query.filter(Producto.precio >= Decimal(precio_min))
    
    # Filtrar por precio maximo
    if precio_max is not None:
        query = query.filter(Producto.precio <= Decimal(precio_max))

    # Busqueda
    if search:
        query = query.filter(Producto.nombre.ilike(f"%{search}"))

    
    # Filtrar los productos
    productos = query.offset(skip).limit(limit).all()

    # Retornar productos
    return productos

# Obtener detalles de el producto
@router.get("/productos/{producto_id}", response_model=ProductoOut)
def detalle_producto(
    producto_id: int,
    db: Session = Depends(get_db)
):
    # Obtener producto por el id
    producto = db.query(Producto).filter(Producto.id == producto_id).first()

    # Excepcion por si no lo encuentra
    if not producto:
        raise HTTPException(status_code= 404, detail= "Producto no encontrado")
    
    return producto

# ENDPOINT DE VALORACIONES
@router.get("/producto/{producto_id}", response_model=List[ValoracionOut])
def valoraciones_del_producto(producto_id: int, db: Session = Depends(get_db)):
    return db.query(Valoraciones).filter_by(producto_id=producto_id).order_by(Valoraciones.fecha.desc()).all()
