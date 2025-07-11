from app.database.base import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nombres = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    correo = Column(String, unique=True, index=True, nullable=False)
    contraseña = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = Column(Boolean, default=True)

    carrito = relationship("Carrito", uselist=False, back_populates="usuario", cascade="all, delete-orphan")
    pedidos = relationship("Pedido", back_populates="usuario", cascade="all, delete-orphan")
    direcciones = relationship("DireccionEnvio", back_populates="usuario", cascade="all, delete-orphan")
    metodos_pago = relationship("MetodoPago", back_populates="usuario", cascade="all, delete-orphan")
    whislist = relationship("ListaDeseos", back_populates="usuario", cascade="all, delete-orphan")
    # vendedor = relationship("Vendedor", uselist=False, back_populates="usuario")

class DireccionEnvio(Base):
    __tablename__ = "direcciones_envio"

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("users.id"))
    direccion = Column(String, unique=True, nullable=False)
    ciudad =Column(String, nullable=False)
    departamento =Column(String, nullable=False)
    pais = Column(String, nullable=False)
    codigo_postal =Column(String)
    telefono =Column(String, unique=True)

    usuario = relationship("User", back_populates="direcciones")

class MetodoPago(Base):
    __tablename__ = "metodos_pago"

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("users.id"))
    alias = Column(String)
    tipo = Column(String)
    detalles = Column(String)

    usuario = relationship("User", back_populates="metodos_pago")

class ListaDeseos(Base):
    __tablename__ = "listas_deseos"

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("users.id"))
    producto_id = Column(Integer, ForeignKey("productos.id"))

    usuario = relationship("User", back_populates="whislist")
    producto = relationship("Producto")
