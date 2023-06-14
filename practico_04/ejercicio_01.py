"""Base de Datos SQL - Crear y Borrar Tablas"""

import sqlite3

def crear_tabla():
    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (autoincremental)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - Altura: Int()
    """
    pass # Completar
    conn = sqlite3.connect("practico04.db")

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Personas (
        idPersona INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(30),
        fechaNacimiento DATE,
        dni INTEGER,
        altura INTEGER
        )''')

    conn.commit()
    conn.close()


def borrar_tabla():
    """Implementar la funcion borrar_tabla, que borra la tabla creada
    anteriormente."""
    pass # Completar
    conn = sqlite3.connect("practico04.db")

    cursor = conn.cursor()

    cursor.execute('''
        DROP TABLE Personas
        ''')

    conn.commit()
    conn.close()

# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
