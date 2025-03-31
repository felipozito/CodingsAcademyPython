""" 
Cree un archivo de python con el nombre taller1_ejercicio1.py 
Se requiere que el estudiante realice comentarios, al menos 2 formas de escribir comentarios en python. 
Creará 4 variables cumpliendo el estándar correcto de Nombres de variables, 2 variables de manera correcta y 2 variables de manera incorrecta, debe comentar las 2 variables incorrectas para que no le de error el código.
Mostrar por pantalla las dos variables que son correctas, haciendo uso de la función de salida de datos print(). 
Deberá obtener el nombre y la edad de una persona ingresando por teclado los datos, hacer uso de la función de entrada de datos input() además deberá mostrar en pantalla los datos ingresados haga uso de la función de salida de datos print(). 
"""
#Variables correctas
nombre = "Juan"
edad = 20
#Variables incorrectas
#! 1nombre = "Juan"
#! %edad1 = 20
nombre=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))
#Mostrar por pantalla las dos variables que son correctas, haciendo uso de la función de salida de datos print().
print(f"El nombre es {nombre} y la edad es {edad}")

