"""
Variables en Python son nombres que pueden tomar cualquier valor. 
Las variables pueden ser de cualquier tipo de datos, como enteros, flotantes, cadenas de caracteres, etc.
Por ejemplo, si queremos almacenar el valor de un número entero en una variable, podemos hacerlo de la siguiente manera:
"""
var=2 #esto es un valor entero
palabra="Hola" #esto es una cadena de caracteres
number=10.2 #esto es un valor flotante
array=[1,2,3,4,5,6,7,8,9,0]   #esto es un array o lista
print(array[0:2])

diccionario={"nombre":"Juan","edad":25} #esto es un diccionario similar a objetos en JavaScript
conjunto={1,2,3,4,5}    #esto es un conjunto o set en Python que almacena un conjunto de valores únicos NO SE MODIFICA 
tupla=(1,2,3,4,5)       #esto es una tupla similar a un array en Python pero inmutable NO SE MODIFICA 
print(tupla)
var=1
"""
Existen limitantes al nombrar variables en Python.
1. No se puede nombrar una variable con un número al inicio.
2. No se puede nombrar una variable con un guión medio al final.
3. No se pueden usar caracteres especiales en las variables.
4. No se pueden usar espacios en las variables.
5. No se pueden usar números en las variables.
6. No se pueden usar signos de puntuación en las variables.
7. No se pueden usar signos de coma en las variables.
"""

#print(palabra[1:2])

diccionario["nombre"]="Felipe"
#print(diccionario)
"""
print(diccionario)
print(type(var))
print(type(palabra))
print(type(number))
print(type(array))
print(type(diccionario))
print(type(conjunto))
print(type(tupla))"""


