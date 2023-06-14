"""Base de Datos SQL - Modificación"""

import datetime
import sqlite3

from practico_04.ejercicio_01 import reset_tabla
from practico_04.ejercicio_02 import agregar_persona
from practico_04.ejercicio_04 import buscar_persona


def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    """Implementar la funcion actualizar_persona, que actualiza un registro de
    una persona basado en su id. Devuelve un booleano en base a si encontro el
    registro y lo actualizo o no."""
    pass # Completar
    persona = (id_persona, nombre, nacimiento, dni, altura)
    conn = sqlite3.connect("practico04.db")
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Personas
        SET idPersona = :id_persona, nombre = :nombre, fechaNacimiento = :nacimiento, dni = :dni, altura = :altura
        WHERE idPersona == :id_persona
        ''', persona)
    registro_actualizado = cursor.rowcount
    conn.commit()
    conn.close()
    return registro_actualizado > 0


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', '1988-04-16 00:00:00', 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
