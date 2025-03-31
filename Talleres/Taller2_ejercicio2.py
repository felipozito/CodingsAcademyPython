"""Cree un archivo de python con el nombre taller2_ejercicio2.py 
1). Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
2). El SRI solicita desarrollar un software que pregunte al usuario su nombre y su ingreso mensual y que calcule un tasa de impuesto segun el salario, ej. 
Si el salario es menor a 1000 se debe debitar un 10% y debe mostrar por pantalla el ingreso mensual, el valor del impuesto y el valor total a recibir.
Si el salario es mayor a 1200 se debe debitar 15% de su salario y un 2.2% por servicios profesionales mostrar el valor a recibir y el valor del impuesto.
Si el salario es mayor a 5000 cobrar un 25% de impuesto y un 5% de retención, muestre el valor a debitar y el valor a recibir.
"""
password1="Felo"
password=input("Ingrese la contraseña: ")
print("it's OK" if password.lower()==password1.lower() else "it's not OK")

name=input("Ingrese su nombre: ")
income=float(input("Ingrese su ingreso mensual: "))
if income<1000:
    tax=income*0.1
    total=income-tax
    print(f"El ingreso mensual es {income}, el valor del impuesto es {tax} y el valor total a recibir es {total}")
if income>1200:
    tax=income*0.15
    total=income-tax
    print(f"El ingreso mensual es {income}, el valor del impuesto es {tax} y el valor total a recibir es {total}")
if income>5000:
    tax=income*0.25
    total=income-tax
    print(f"El ingreso mensual es {income}, el valor del impuesto es {tax} y el valor total a recibir es {total}")
    