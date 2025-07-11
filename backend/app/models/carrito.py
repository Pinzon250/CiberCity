from sqlalchemy import Column, Integer, ForeignKey, String  , Boolean, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.base import Base

class Carrito(Base):
    __tablename__ = "carritos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("users.id"), unique=True)
    cupon_codigo = Column(String, nullable=True)

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
    items = relationship("PedidoItem", back_populates="pedido", cascade="all, delete")

class Cupon(Base):
    __tablename__ = "cupones"

    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String, unique=True, index=True)
    descuento = Column(DECIMAL(5, 2), nullable=False)
    activo = Column(Boolean, default=True)

    fecha_expiracion = Column(DateTime, nullable=False)
    max_usos_por_usuario = Column(Integer, default=1)
    max_usos_global = Column(Integer, nullable=True)

    usos = relationship("CuponUso", back_populates="cupon", cascade="all, delete")

class CuponUso(Base):
    __tablename__ = "cupon_usos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("users.id"))
    cupon_id = Column(Integer, ForeignKey("cupones.id"))
    fecha_uso = Column(DateTime, default=datetime.utcnow)

    cupon = relationship("Cupon", back_populates="usos")

class PedidoItem(Base):
    __tablename__ = "pedido_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"))
    producto_id = Column(Integer, ForeignKey("productos.id"))
    cantidad = Column(Integer, default=1)
    precio_unitario = Column(DECIMAL(10, 2))

    pedido = relationship("Pedido", back_populates="items")
    producto = relationship("Producto")