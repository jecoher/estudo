from backend.aplicacion.modelos.producto import Producto
from backend.aplicacion.repositorios.producto_repository import ProductRepository
from backend.aplicacion.servicios.product_service import ProductService
from aplicacion.excepciones.producto_excepciones import ProductoDuplicadoError


repositorio = ProductRepository()
servicio = ProductService(repositorio)

# Crear la tabla si todavía no existe
repositorio.crear()

# Crear un producto de prueba
producto = Producto(
    nombre="Cemento Portland",
    unidad_medida="KG",
    categoria="Construccion",
    subcategoria="Cemento"
)
try:
    resultado = servicio.guardar(producto)
    print(resultado)
except ProductoDuplicadoError as error:
    print(f'Error de negocio: {error}')

