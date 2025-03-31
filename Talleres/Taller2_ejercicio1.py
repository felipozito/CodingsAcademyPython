"""
El SRI solicita un software para tributar un determinado impuesto:

Cree un archivo de python con el nombre taller2_ejercicio1.py 
El software debe solicitar el nombre, edad y el ingreso mensual de una persona.
El software debe evaluar si la persona es mayor de edad o menor de edad.
El software debe evaluar si el ingreso mensual es mayor a 2000 USD.
El software debe mostrar el siguiente mensaje “Estimado usuario: nombreDelUsuario ud. debe tributar” en caso de que la persona sea mayor de edad. 
El software debe mostrar un mensaje cuando el ingreso sea menor a 500 USD y la persona sea mayor de edad, el mensaje dirá lo siguiente:  “Estimado usuario: nombreDelUsuario ud. No debe pagar impuestos”. 
El software debe mostrar el nombre de la persona, la edad y un mensaje que diga, Estimado usuario ud. no es apto para tributar. 
"""
name=input("Ingrese su nombre: ")
age=int(input("Ingrese su edad: "))
income=int(input("Ingrese su ingreso mensual: "))
if age<18:
     print(f"Estimado usuario: {name} ud. no es apto para tributar")
else:
    if income>2000:
        print(f"Estimado usuario: {name} ud. debe tributar")
    if income<=500:
        print(f"Estimado usuario: {name} ud. No debe pagar impuestos")

        
