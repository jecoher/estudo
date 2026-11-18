# from backend.aplicacion.repositorios.producto_repository import ProductRepository
# from backend.aplicacion.modelos.producto import Producto
from fastapi import FastAPI

app = FastAPI(
    title='ERP Empresarial',
    description='API principal del sistema',
    version='1.0.0'
)

@app.get('/')
def inicio():
    return {'mensaje': 'Bienvenido al ERP Empresarial'}

# repositorio = ProductRepository()

# buscar = repositorio.buscar_por_nombre('cemento')
# print(buscar)