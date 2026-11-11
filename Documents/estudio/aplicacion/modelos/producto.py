from dataclasses import dataclass

@dataclass
class Producto:
    nombre: str
    unidad_medida: str
    categoria: str
    subcategoria: str
    id: int = None

    
    def __post_init__(self):
        nombre = self.nombre.strip() .upper()
        unidad_medida = self.unidad_medida.strip() .upper()
        categoria = self.categoria.strip() .upper()
        subcategoria = self.subcategoria.strip() .upper()