from dataclasses import dataclass, asdict
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

# lista = []

# n= Producto('espude', 'un', 'accesorio', 'ferramentas')
# o= Producto('joelho 25 sold', 'un', 'conecciones', 'ferramentas')
# p= Producto('caixa cd 24m', 'un', 'accesorio', 'eletrico')
# q= Producto('fita vedarosca 10', 'un', 'accesorio', 'canos')
# lista.append(n)
# lista.append(o)
# lista.append(p)
# lista.append(q)

# nueva_lista = [asdict(producto) for producto in lista]

# for producto in nueva_lista:
#     print(producto)


