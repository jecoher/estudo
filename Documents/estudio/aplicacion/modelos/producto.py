from dataclasses import dataclass

@dataclass
class Producto:
    nombre: str
    unidad_medida: str
    categoria: str
    subcategoria: str
    id: int = None

    

