"""Escribir un programa de operaciones matematicas básicas, que por cada operación cree una funcion para realizar el proceso, luego cree una funcion donde muestre los resultados de las funciones.

"""
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    return a/b
def imprimir(a,b):
    print("La suma de los dos numeros es: ",suma(a,b))
    print("La resta de los dos numeros es: ",resta(a,b))
    print("La multiplicacion de los dos numeros es: ",multiplicacion(a,b))
    print("La division de los dos numeros es: ",division(a,b))
    
imprimir(5,5)