db=[{
    "id":"1",
    "name":"Felipe",
    "apellido":"Gonzalez",
    "Salario":1200,
    "cargo":"x"
}]
def listarUsuario(db):
    print(db)
    
def agregarUsuario(db):
    user={}
    user["id"]=input("Ingrese el id: ")
    user["name"]=input("Ingrese el nombre: ")
    user["apellido"]=input("Ingrese el apellido: ")
    user["Salario"]=input("Ingrese el salario: ")
    user["cargo"]=input("Ingrese el cargo: ")
    db.append(user)
    print("Se Agrego el usuario con exito")
    
def eliminarUsuario(db):
    id=input("Ingrese el id del usuario que desea eliminar: ")
    for i, user in enumerate(db):
        if user["id"]==id:
            db.pop(i)
            print("Se elimino el usuario con exito")
            return 
    print("No se encontro el usuario")
def actualizarUsuario(db):
    id=input("Ingrese el id del usuario que desea actualizar: ")
    for i, user in enumerate(db):
        if user["id"]==id:
            user["name"]=input("Ingrese el nombre: ")
            user["apellido"]=input("Ingrese el apellido: ")

def main():
    empleados = db
    while True:
        print("\n=== SISTEMA DE GESTIÓN DE EMPLEADOS ===")
        print("1. Agregar empleado")
        print("2. Listar empleados")
        print("3. Buscar empleado")
        print("4. Actualizar empleado")
        print("5. Eliminar empleado")
        print("6. Salir")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            agregarUsuario(empleados)
        elif opcion == "2":
            listarUsuario(empleados)
        elif opcion == "3":
            buscar_empleado(empleados)
        elif opcion == "4":
            actualizarUsuario(empleados)
        elif opcion == "5":
            eliminarUsuario(empleados)
        elif opcion == "6":
            print("\n¡Hasta luego! 👋")
            break
        else:
            print("\n❌ Opción inválida. Intenta nuevamente.")
               
main()
