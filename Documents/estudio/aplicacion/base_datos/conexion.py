import sqlite3

class Conexion:
    def __init__(self, dbname='database.db'):
        self.dbname = dbname

    def conectar(self):
        try:
            conn = sqlite3.connect(self.dbname)
            cursor = conn.cursor()

            return conn, cursor
        except sqlite3.Error as error:
            print(f'Error: {error}')
            raise


