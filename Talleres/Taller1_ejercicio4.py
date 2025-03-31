        
"""El distrito metropolitano de Quito requiere un programa que solicite al usuario el ingreso de dos números diferentes y muestre en pantalla el mayor de los dos.
    """
x,y=int(input("Ingrese un numero: ")),int(input("Ingrese un numero: "))
while x == y:
    x,y=int(input("Ingrese un numeros diferentes: "),input("Ingreseun numeros diferentes: "))   
if x>y:
    print(f"El numero mayor es {x}")
else:
    print(f"El numero mayor es {y}")