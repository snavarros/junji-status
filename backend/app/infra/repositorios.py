from sqlalchemy.orm import Session
from app.infra import models


class UsuarioRepositorio:
    def __init__(self, db: Session):
        self.db = db

    def crear(self, correo: str, telefono: str = None):
        usuario = models.Usuario(correo=correo, telefono=telefono)
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    def activar(self, usuario_id: int):
        usuario = self.db.query(models.Usuario).get(usuario_id)
        usuario.activo = True
        self.db.commit()
        return usuario


class EstablecimientoRepositorio:
    def __init__(self, db: Session):
        self.db = db

    def listar(self):
        return self.db.query(models.Establecimiento).all()


class ReporteRepositorio:
    def __init__(self, db: Session):
        self.db = db

    def crear(
        self,
        usuario_id: int,
        est_id: int,
        descripcion: str,
        categoria: str,
        afecta_total: bool,
    ):
        reporte = models.Reporte(
            usuario_id=usuario_id,
            establecimiento_id=est_id,
            descripcion=descripcion,
            categoria=categoria,
            afecta_total=afecta_total,
        )
        self.db.add(reporte)

        # actualizar estado del establecimiento
        est = self.db.query(models.Establecimiento).get(est_id)
        est.estado = "con_problema"

        self.db.commit()
        self.db.refresh(reporte)
        return reporte
