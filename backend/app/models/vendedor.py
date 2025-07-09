# from sqlalchemy import Column, Integer, String, Enum, ForeignKey
# from sqlalchemy.orm import relationship
# from app.database.connection import Base
# import enum

# class TipoVendedorEnum(str, enum.Enum):
#     oficial = "oficial"
#     interno = "interno"
#     tercero = "tercero"

# class Vendedor(Base):
#     __tablename__ = "vendedores"

#     id = Column(Integer, primary_key=True, index=True)
#     nombre_tienda = Column(String(255), nullable=False)
#     tipo = Column(Enum(TipoVendedorEnum), nullable=False)

#     usuario_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=True)
#     productos = relationship("Producto", back_populates="vendedor", cascade="all, delete-orphan")
#     usuario = relationship("User", back_populates="vendedor")
