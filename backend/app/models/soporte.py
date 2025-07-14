from app.database.base import Base
from sqlalchemy import Column, Integer, Text, String, Table, DateTime, String, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship
from datetime import datetime

class MensajeContacto(Base):
    __tablename__ = "mensajes_contacto"

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("users.id"))
    asunto = Column(String(150))
    mensaje = Column(Text)
    fecha =Column(DateTime, default=datetime.utcnow)

    usuario = relationship("User")

class FAQ(Base):
    __tablename__ = "faqs"

    id = Column(Integer, primary_key=True)
    pregunta = Column(String(255))
    respuesta = Column(Text)

promocion_producto = Table(
    'promocion_producto',
    Base.metadata,
    Column('promocion_id', Integer, ForeignKey('promociones.id')),
    Column('producto_id', Integer, ForeignKey('productos.id'))
)

promocion_categoria = Table(
    'promocion_categoria',
    Base.metadata,
    Column('promocion_id', Integer, ForeignKey('promociones.id')),
    Column('categoria_id', Integer, ForeignKey('categorias.id'))
)

class Promocion(Base):
    __tablename__ = "promociones"

    id = Column(Integer, primary_key=True)
    titulo = Column(String(100))
    descripcion = Column(Text)
    descuento_procentaje= Column(Float)
    fecha_inicio = Column(DateTime, default=datetime.utcnow)
    fecha_fin = Column(DateTime)
    activa = Column(Boolean, default=True)

    productos = relationship("Producto", secondary=promocion_producto, back_populates="promociones")
    categorias = relationship("Categoria", secondary=promocion_categoria, back_populates="promociones")
