"""Base de Datos SQL - Creación de tablas auxiliares"""
import sqlite3

from practico_04.ejercicio_01 import borrar_tabla, crear_tabla


def crear_tabla_peso():
    """Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
        - IdPersona: Int() (Clave Foranea Persona)
        - Fecha: Date()
        - Peso: Int()
    """
    pass # Completar
    conn = sqlite3.connect("practico04.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS PersonaPeso (
        idPersona INTEGER,
        fecha DATE,
        peso INTEGER,
        FOREIGN KEY (idPersona) REFERENCES Personas(idPersona)
        )''')
    conn.commit()
    conn.close()


def borrar_tabla_peso():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    pass # Completar
    conn = sqlite3.connect("practico04.db")
    cursor = conn.cursor()
    cursor.execute('''
        DROP TABLE PersonaPeso
    ''')
    conn.commit()
    conn.close()

# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
