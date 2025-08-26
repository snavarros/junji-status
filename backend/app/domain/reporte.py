from dataclasses import dataclass
from enum import Enum
from datetime import datetime


class EstadoEstablecimiento(str, Enum):
    NORMAL = "normal"
    PARCIAL = "parcial"
    CERRADO = "cerrado"


class CausaIncidencia(str, Enum):
    DESASTRE_NATURAL = "desastre_natural"
    PARO = "paro"
    INCIDENCIA = "incidencia"
    FUGA = "fuga"
    OTRO = "otro"


@dataclass
class Reporte:
    id: int
    establecimiento_id: int
    usuario_id: int
    estado: EstadoEstablecimiento
    causa: CausaIncidencia
    descripcion: str
    fecha_inicio: datetime
    fecha_fin: datetime | None = None
