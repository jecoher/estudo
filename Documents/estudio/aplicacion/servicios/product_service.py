from aplicacion.repositorios.producto_repository import ProductRepository
import sqlite3

class ProductService:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def guardar(self, objeto):
        encontrado = self.repositorio.buscar_por_nombre(objeto.nombre)
        if encontrado != []:
            return f'Producto ya registrado!'
        try:
            return self.repositorio.guardar(objeto)
        except sqlite3.IntegrityError as error:
            return f'Producto ya registrado! {error}'
        except sqlite3.Error as error:
            return f'Falla en la base de datos {error}'

        


