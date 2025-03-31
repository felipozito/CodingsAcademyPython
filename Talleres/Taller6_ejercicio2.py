"""Crear dos clases una para administrar los contactos, con el método de crear contato y monstrar contacto. 
La segunda clase debe acceder a la primera clase y tener un nuevo metodo que permita eliminar registros. 
"""
class Contacto:
    def __init__(self):
        self.contactos = []
    def crear_contacto(self, nombre, telefono, correo):
        contacto = {
            "nombre": nombre,
            "telefono": telefono,
            "correo": correo
        }
        self.contactos.append(contacto)
        print("Contacto creado exitosamente.")
    def mostrar_contactos(self):
        print("Contactos:")
        for contacto in self.contactos:
            print(f"Nombre: {contacto['nombre']}")
            print(f"Teléfono: {contacto['telefono']}")
            print(f"Correo: {contacto['correo']}")
            print("------------------------")
class AdministrarContactos:
    def __init__(self):
        self.contacto = Contacto()
    def eliminar_contacto(self, nombre):
        for contacto in self.contacto.contactos:
            if contacto["nombre"] == nombre:
                self.contacto.contactos.remove(contacto)
                print("Contacto eliminado exitosamente.")
                return
        print("Contacto no encontrado.")
# Ejemplo de uso
administrar_contactos = AdministrarContactos()
administrar_contactos.contacto.crear_contacto("Juan Perez", "1234567890",print("Contacto no encontrado."))
# Ejemplo de uso
administrar_contactos = AdministrarContactos()
administrar_contactos.contacto.crear_contacto("Juan Perez", "1234567890", "EMAIL")  