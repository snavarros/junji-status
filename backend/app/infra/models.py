from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from app.infra.db import Base
from datetime import datetime


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    correo = Column(String, unique=True, index=True, nullable=False)
    telefono = Column(String, nullable=True)
    activo = Column(Boolean, default=False)

    reportes = relationship("Reporte", back_populates="usuario")


class Establecimiento(Base):
    __tablename__ = "establecimientos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    codigo = Column(String, unique=True, nullable=False)
    latitud = Column(String, nullable=True)
    longitud = Column(String, nullable=True)
    estado = Column(String, default="normal")

    reportes = relationship("Reporte", back_populates="establecimiento")


class Reporte(Base):
    __tablename__ = "reportes"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    establecimiento_id = Column(Integer, ForeignKey("establecimientos.id"))
    descripcion = Column(Text, nullable=False)
    categoria = Column(String, nullable=False)  # desastre, paro, incidencia, etc.
    afecta_total = Column(Boolean, default=False)
    fecha_inicio = Column(DateTime, default=datetime.utcnow)
    fecha_fin = Column(DateTime, nullable=True)

    usuario = relationship("Usuario", back_populates="reportes")
    establecimiento = relationship("Establecimiento", back_populates="reportes")
