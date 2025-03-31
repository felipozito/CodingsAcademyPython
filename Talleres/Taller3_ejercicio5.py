"""Crear un sistema que permita registrar, actualizar y eliminar las frutas para un sistema de la fruteria Fruta Golosa S.A. Debe utilizar lo siguiente:

1.- Comentarios.
2.- input, print 
3.- listas 
4.- Condicionales if y else 
5.- For (de ser necesario)
6.- While (de ser necesario? 

El sistema debe tener un menú de opciones (1.- Registrar, 2.- Actualizar, 3.- Eliminar y 4. - Salir del sistema)
"""

# Sistema de gestión de frutas para Fruta Golosa S.A.
# Este programa permite registrar, actualizar y eliminar frutas del inventario

# Inicializamos la lista de frutas con algunos ejemplos
frutas = ["Manzana", "Banana", "Naranja", "Pera", "Uva"]

def mostrar_frutas():
    """Función para mostrar todas las frutas en el inventario"""
    print("\n=== INVENTARIO DE FRUTAS ===")
    if len(frutas) == 0:
        print("No hay frutas registradas en el inventario.")
    else:
        for i, fruta in enumerate(frutas):
            print(f"{i+1}. {fruta}")
    print("===========================\n")

def registrar_fruta():
    """Función para registrar una nueva fruta en el inventario"""
    nueva_fruta = input("Ingrese el nombre de la fruta a registrar: ")
    # Verificamos si la fruta ya existe en el inventario
    if nueva_fruta in frutas:
        print(f"¡La fruta '{nueva_fruta}' ya existe en el inventario!")
    else:
        frutas.append(nueva_fruta)
        print(f"¡La fruta '{nueva_fruta}' ha sido registrada exitosamente!")
    
    mostrar_frutas()

def actualizar_fruta():
    """Función para actualizar una fruta existente en el inventario"""
    mostrar_frutas()
    
    if len(frutas) == 0:
        return
    
    try:
        indice = int(input("Ingrese el número de la fruta que desea actualizar: ")) - 1
        
        # Verificamos si el índice es válido
        if 0 <= indice < len(frutas):
            fruta_actual = frutas[indice]
            nueva_fruta = input(f"Ingrese el nuevo nombre para '{fruta_actual}': ")
            
            frutas[indice] = nueva_fruta
            print(f"¡La fruta ha sido actualizada de '{fruta_actual}' a '{nueva_fruta}'!")
        else:
            print("¡Número de fruta inválido!")
    except ValueError:
        print("¡Por favor ingrese un número válido!")
    
    mostrar_frutas()

def eliminar_fruta():
    """Función para eliminar una fruta del inventario"""
    mostrar_frutas()
    if len(frutas) == 0:
        return
    try:
        indice = int(input("Ingrese el número de la fruta que desea eliminar: ")) - 1
        
        # Verificamos si el índice es válido
        if 0 <= indice < len(frutas):
            fruta_eliminada = frutas.pop(indice)
            print(f"¡La fruta '{fruta_eliminada}' ha sido eliminada exitosamente!")
        else:
            print("¡Número de fruta inválido!")
    except ValueError:
        print("¡Por favor ingrese un número válido!")
    
    mostrar_frutas()

def menu_principal():
    """Función que muestra el menú principal del sistema"""
    print("\n===== SISTEMA DE GESTIÓN DE FRUTAS =====")
    print("===== FRUTA GOLOSA S.A. =====")
    print("1. Registrar fruta")
    print("2. Actualizar fruta")
    print("3. Eliminar fruta")
    print("4. Salir del sistema")
    print("=======================================")
# Ciclo principal del programa
while True:
    menu_principal()
    opcion = input("Seleccione una opción (1-4): ")
    if opcion == "1":
        registrar_fruta()
    elif opcion == "2":
        actualizar_fruta()
    elif opcion == "3":
        eliminar_fruta()
    elif opcion == "4":
        print("\n¡Gracias por utilizar el sistema de Fruta Golosa S.A.!")
        break
    else:
        print("\n¡Opción inválida! Por favor seleccione una opción del 1 al 4.")
