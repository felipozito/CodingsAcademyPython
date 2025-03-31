"""Crear una clase Persona que incorpore el metodo constructor, un método para añadir registros y otro para mostrar registros.
"""

class Persona:
    def __init__(self):
        self.registros = []
    def agregar_registro(self, registro):
        self.registros.append(registro)
    def mostrar_registros(self):
        print("Registros:")
        for registro in self.registros:
            print(registro)
# Ejemplo de uso
persona = Persona()
persona.agregar_registro("Registro 1")
persona.agregar_registro("Registro 2")
persona.mostrar_registros()
            