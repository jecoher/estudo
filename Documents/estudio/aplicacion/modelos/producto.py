from dataclasses import dataclass

@dataclass
class Producto:
    nombre: str
    unidad_medida: str
    categoria: str
    subcategoria: str
    id: int = None

    
    def __post_init__(self):
        self.nombre = self.nombre.strip() .upper()
        self.unidad_medida = self.unidad_medida.strip() .upper()
        self.categoria = self.categoria.strip() .upper()
        self.subcategoria = self.subcategoria.strip() .upper()

