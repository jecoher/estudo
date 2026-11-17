from aplicacion.base_datos.conexion import Conexion
from aplicacion.modelos.producto import Producto

import sqlite3


class ProductRepository:
    def __init__(self):
        self.conexion = Conexion()

    @staticmethod
    def cambio_a_objeto(registro):
        return Producto(
            id=registro[0],
            nombre=registro[1],
            unidad_medida=registro[2],
            categoria=registro[3],
            subcategoria=registro[4]
        )
    
    def crear(self):
        conn, cursor = self.conexion.conectar()
        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL UNIQUE,
                    unidad_medida TEXT NOT NULL,
                    categoria TEXT NOT NULL,
                    subcategoria TEXT NOT NULL
                )
            ''')
            conn.commit()
        except sqlite3.Error:
            conn.rollback()
            raise
        finally:
            cursor.close()
            conn.close()    

    def guardar(self, objeto_producto) -> object:
        conn, cursor = self.conexion.conectar()
        try:
            instruccion = ('INSERT INTO productos (nombre, unidad_medida, categoria, subcategoria) VALUES (?,?,?,?)')
            valores = (objeto_producto.nombre, objeto_producto.unidad_medida, objeto_producto.categoria, objeto_producto.subcategoria)
            cursor.execute(instruccion, valores)
            objeto_producto.id = cursor.lastrowid
            conn.commit()
            return objeto_producto
        finally:
            cursor.close()
            conn.close()

    def buscar_por_id(self, id_buscar) -> object:
        if type(id_buscar) is not int or id_buscar <= 0:
            return None
        else:
            conn, cursor = self.conexion.conectar()
            try:
                instruccion = 'SELECT * FROM productos WHERE id = ?'
                valores = (id_buscar,)
                cursor.execute(instruccion, valores)
                encontrado = cursor.fetchone()
                if encontrado is not None:
                    tupla_a_objeto = self.cambio_a_objeto(encontrado)
                    return tupla_a_objeto
                return None
            except sqlite3.Error as error:
                raise
            finally:
                cursor.close()
                conn.close()
        
    def buscar_por_nombre(self, nombre_buscar) -> object:
        '''
        >>> list() vacia si atributo no encontrado
        '''
        if not nombre_buscar:
            return []
        else:
            nombre_buscar = nombre_buscar.strip() .upper()
            nombre_buscar = nombre_buscar.split()
            conn, cursor = self.conexion.conectar()
            condiciones = []
            valores = []
            for p in nombre_buscar:
                condiciones.append('nombre LIKE ?')
                valores.append(f'%{p}%')

            consulta = ' AND '.join(condiciones)
            try:
                instruccion = f'SELECT * FROM productos WHERE {consulta}'
                cursor.execute(instruccion, valores)
                resultado = cursor.fetchall()
                if not resultado:
                    return []

                lista_objetos_encontrados = []
                for item in resultado:
                    item_a_objeto = self.cambio_a_objeto(item)
                    lista_objetos_encontrados.append(item_a_objeto)
                return lista_objetos_encontrados
            except sqlite3.Error as error:
                raise
            finally:
                cursor.close()
                conn.close()
    


