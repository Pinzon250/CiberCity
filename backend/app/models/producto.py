from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.base import Base
from .soporte import promocion_producto

class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(Text)
    precio = Column(Numeric(10, 2), nullable=False)
    stock = Column(Integer, default=0)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)

    # Relaciones
    # vendedor_id = Column(Integer, ForeignKey("vendedores.id"), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))

    # vendedor = relationship("Vendedor", back_populates="productos")
    promociones = relationship("Promocion", secondary=promocion_producto, back_populates="productos")
    valoraciones = relationship("Valoraciones", back_populates="producto", cascade="all, delete")
    categoria = relationship("Categoria", back_populates="productos")
    atributos = relationship("ProductoAtributo", back_populates="producto", cascade="all, delete")
    imagenes = relationship("ImagenProducto", back_populates="producto", cascade="all, delete")

class ImagenProducto(Base):
    __tablename__ = "imagenes_producto"
    id = Column(Integer, primary_key=True, index=True)
    imagen = Column(String, nullable=False)

    producto_id = Column(Integer, ForeignKey("productos.id"))
    producto = relationship("Producto", back_populates="imagenes")


