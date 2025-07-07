from sqlalchemy import Column, Integer, ForeignKey, Table, Boolean, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.connection import Base

class Carrito(Base):
    __tablename__ = "carritos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("users.id"), unique=True)

    usuario = relationship("User", back_populates="carrito")
    items = relationship("CarritoItem", back_populates="carrito", cascade="all, delete-orphan")


class CarritoItem(Base):
    __tablename__ = "carrito_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    carrito_id = Column(Integer, ForeignKey("carritos.id"))
    producto_id = Column(Integer, ForeignKey("productos.id"))
    cantidad = Column(Integer, default=1)

    carrito = relationship("Carrito", back_populates="items")
    producto = relationship("Producto")


class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("users.id"))
    total = Column(DECIMAL(10, 2), nullable=False)
    pagado = Column(Boolean, default=False)
    fecha_pedido = Column(DateTime, default=datetime.utcnow)

    usuario = relationship("User", back_populates="pedidos")