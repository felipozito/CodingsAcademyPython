"""Al planteamiento #1, agregarle lo siguiente:
Agregue un menú de opciones, cuando el usuario digite la palabra suma, realice la operacion de suma, cuando el usuario digite resta realice la operacion de resta y asi con las demas operaciones multiplicacion y division.
"""
def suma(num1,num2):
    return num1+num2
def resta(num1,num2):
    return num1-num2
def multiplicacion(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2
def menu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    opcion=int(input("Ingrese una opcion: "))
    return opcion
def main():
    opcion=menu()
    while opcion!=5:
        if opcion==1:
            num1=int(input("Ingrese el primer numero: "))
            num2=int(input("Ingrese el segundo numero: "))
            print("La suma de los dos numeros es: ",suma(num1,num2))
        elif opcion==2:
            num1=int(input("Ingrese el primer numero: "))
            num2=int(input("Ingrese el segundo numero: "))
            print("La resta de los dos numeros es: ",resta(num1,num2))
        elif opcion==3:
            num1=int(input("Ingrese el primer numero: "))
            num2=int(input("Ingrese el segundo numero: "))
            print("La multiplicacion de los dos numeros es: ",multiplicacion(num1,num2))    
        elif opcion==4:
            num1=int(input("Ingrese el primer numero: "))
            num2=int(input("Ingrese el segundo numero: "))
            print("La division de los dos numeros es: ",division(num1,num2))
        else:
            print("Opcion no valida")
        opcion=menu()
main()  