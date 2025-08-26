from dataclasses import dataclass
from enum import Enum


class RolUsuario(str, Enum):
    NORMAL = "normal"
    ADMIN_REGIONAL = "admin_regional"
    DIRNAC = "dirnac"


@dataclass
class Usuario:
    id: int
    nombre: str
    email: str
    celular: str
    activo: bool = False
    rol: RolUsuario = RolUsuario.NORMAL
    establecimiento_id: int | None = None
