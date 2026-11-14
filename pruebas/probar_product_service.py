from aplicacion.modelos.producto import Producto
from aplicacion.repositorios.producto_repository import ProductRepository
from aplicacion.servicios.product_service import ProductService


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

resultado = servicio.buscar_por_nombre('co')

print("Resultado de guardar:")
print(resultado)