
""" Sabemos que la función input() captura lo que el usuario escribe en el programa, pero el tipo de dato que lee será siempre string. Si necesitamos que sea un número debemos convertir lo que input() captura. Para convertir a número entero usamos int(input()) y para convertir a número con decimales usamos float(input()).

Sabiendo lo siguiente:  El banco de Guayaquil solicita el desarrollo de un software para obtener la suma dos cantidades ingresadas por teclado.

El software evaluará si el resultado de la suma es mayor que 25 deberá mostrar el mensaje con el valor de la suma.
Además deberá mostrar un segundo mensaje que reste 5 al valor de la suma. 
Si el resultado de la resta es menor que 10 que imprima por pantalla” Gracias por su visita, vuelva pronto.” 
"""
x=int(input("Ingrese un numero: "))
y=int(input("Ingrese un numero: "))
suma=x+y
if suma>25:
    print(f"La suma es {suma}")
    resta=suma-5
    print(f"Se resta 5 = {resta}")
    if resta<10:
        print("Gracias por su visita, vuelva pronto.")
