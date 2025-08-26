from sqlalchemy.orm import Session
from app.infra.repositorios import UsuarioRepositorio


def registrar_usuario(db: Session, correo: str, telefono: str = None):
    repo = UsuarioRepositorio(db)
    return repo.crear(correo, telefono)
