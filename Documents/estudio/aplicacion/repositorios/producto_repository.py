from aplicacion.base_datos.conexion import Conexion

import sqlite3
from dataclasses import dataclass

class ProductRepository:
    def __init__(self):
        self.conexion = Conexion()

    def crear(self):
        conn, cursor = self.conexion.conectar()
        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL UNIQUE UNIQUE,
                    unidad_medida TEXT NOT NULL,
                    categoria TEXT NOT NULL,
                    subcategoria TEXT NOT NULL
                )
            ''')
            conn.commit()
        except sqlite3.Error as error:
            conn.rollback()
            print(f'Error al crear la tabla {error}')
            raise
        finally:
            cursor.close()
            conn.close()    

    def guardar(self, objeto_producto):

        conn, cursor = self.conexion.conectar()
        try:
            instruccion = ('INSERT INTO productos (nombre, unidad_medida, categoria, subcategoria) VALUES (?,?,?,?)')
            valores = (objeto_producto.nombre, objeto_producto.unidad_medida, objeto_producto.categoria, objeto_producto.subcategoria)
            cursor.execute(instruccion, valores)
            objeto_producto.id = cursor.lastrowid
            conn.commit()
            print("producto registrado correctamente")
            return objeto_producto
        except sqlite3.IntegrityError as errorIntegridad:
            print(f'ya existe un producto con este nombre! \nError: {errorIntegridad}')
        except sqlite3.Error as error:
            print(f'No fue posible guardar el producto! \nError: {error}')
            raise
        finally:
            cursor.close()
            conn.close()

    # def buscar(self, buscar_nombre):

    

