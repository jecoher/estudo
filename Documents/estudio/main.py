from aplicacion.repositorios.producto_repository import ProductRepository
from aplicacion.modelos.producto import Producto

repositorio = ProductRepository()

buscar = repositorio.buscar_por_nombre('100 joel')
print(buscar)
