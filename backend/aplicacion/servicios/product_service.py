from aplicacion.repositorios.producto_repository import ProductRepository
from aplicacion.excepciones.producto_excepciones import ProductoDuplicadoError
import sqlite3

class ProductService:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def guardar(self, objeto):
        encontrado = self.repositorio.buscar_por_nombre(objeto.nombre)
        if encontrado:
            raise ProductoDuplicadoError('El producto ya esta registrado')
        return self.repositorio.guardar(objeto)

    def buscar_por_id(self, id_buscar):
        return self.repositorio.buscar_por_id(id_buscar)

    def buscar_por_nombre(self, nombre_procurado):
        return self.repositorio.buscar_por_nombre(nombre_procurado)

        


