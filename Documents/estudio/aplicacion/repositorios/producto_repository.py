from aplicacion.base_datos.conexion import Conexion
from aplicacion.modelos.producto import Producto

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

    def buscar_por_id(self, id_buscar):
        if type(id_buscar) is not int or id_buscar <= 0:
            return f'El id del producto debe ser un numero entero!'
        else:
            conn, cursor = self.conexion.conectar()
            try:
                instruccion = 'SELECT * FROM productos WHERE id = ?'
                valores = (id_buscar,)
                cursor.execute(instruccion, valores)
                encontrado = cursor.fetchone()
                if encontrado is not None:
                    tupla_a_objeto = Producto(nombre=encontrado[1], unidad_medida=encontrado[2], categoria=encontrado[3], subcategoria=encontrado[4], id=encontrado[0]) 
                    return tupla_a_objeto
                return None
            except sqlite3.Error as error:
                print(f'Error :{error}')
            finally:
                cursor.close()
                conn.close()
        
    def buscar_por_nombre(self, nombre_buscar):
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
                return resultado
            except sqlite3.Error as error:
                print(f'error: {error}')
            finally:
                cursor.close()
                conn.close()
    

