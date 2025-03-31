# Crea un programa de adivina el numero 

import random

def juego_adivinanza():
    numero_secreto = random.randint(1, 20)
    vidas = 10
    intentos = 0
    print("Bienvenido al juego de adivinanza.")
    print("Debes adivinar el numero secreto entre 1 y 20.")
    
    while vidas > intentos:
        print("Tienes", ((vidas-intentos) * "o"), "vidas.")
        intentos += 1 
        adivinanza = int(input("Adivina el numero (entre 1 y 20): "))
        if adivinanza < numero_secreto:
            print("El numero es mayor.")
        elif adivinanza > numero_secreto:
            print("El numero es menor.")  
        else:
            print("Felicidades, adivinaste el numero en", intentos, "intentos.")
            break
    print("Fin del juego. El numero secreto era", numero_secreto)

if __name__ == "__main__":
    juego_adivinanza()