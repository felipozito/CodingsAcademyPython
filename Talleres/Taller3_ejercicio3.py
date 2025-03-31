"""Escribir un programa que permita  al usuario ingresar 5 números enteros, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

La variable debe empezar vacia: elementos = []

Utilice (Input, print, int, str, sort, y la sintaxis para añadir elementos a la lista, se permite ser creativo).

"""
nombre=[]
for i in range(5):
    nombre.append(int(input("Ingrese un numero: ")))
nombre.sort()
print(nombre)   