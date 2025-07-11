from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base

class Atributo(Base):
    __tablename__ = "atributos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, nullable=False)

    valores = relationship("ValorAtributo", back_populates="atributo", cascade="all, delete")

class ValorAtributo(Base):
    __tablename__ = "valores_atributo"
    id = Column(Integer, primary_key=True, index=True)
    valor = Column(String, nullable=False)

    atributo_id = Column(Integer, ForeignKey("atributos.id"))
    atributo = relationship("Atributo", back_populates="valores")
    
    productos = relationship("ProductoAtributo", back_populates="valor_atributo", cascade="all, delete")

class ProductoAtributo(Base):
    __tablename__ = "producto_atributos"
    id = Column(Integer, primary_key=True, index=True)

    producto_id = Column(Integer, ForeignKey("productos.id"))
    valor_atributo_id = Column(Integer, ForeignKey("valores_atributo.id"))

    producto = relationship("Producto", back_populates="atributos")
    valor_atributo = relationship("ValorAtributo", back_populates="productos")
