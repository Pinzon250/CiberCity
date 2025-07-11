from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base

class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    padre_id = Column(Integer, ForeignKey("categorias.id"), nullable=True)

    subcategorias = relationship("Categoria", backref="padre", remote_side=[id])
    productos = relationship("Producto", back_populates="categoria")
