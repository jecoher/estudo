from backend.aplicacion.repositorios.producto_repository import ProductRepository
from backend.aplicacion.modelos.producto import Producto

repositorio = ProductRepository()

buscar = repositorio.buscar_por_nombre('cemento')
print(buscar)
