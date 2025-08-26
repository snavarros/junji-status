from dataclasses import dataclass


@dataclass
class Establecimiento:
    id: int
    nombre: str
    region: str
    lat: float
    lon: float
    codigo_registro: str
