import random

def imprimir_tablero(tablero):
    """Imprime el tablero de juego en formato visual."""
    print("\n")
    for i in range(3):
        print(f" {tablero[i*3]} | {tablero[i*3+1]} | {tablero[i*3+2]} ")
        if i < 2:
            print("-----------")
    print("\n")

def hay_ganador(tablero):
    """Verifica si hay un ganador en el tablero actual."""
    # Verificar filas y columnas
    for i in range(3):
        # Filas
        if tablero[i*3] == tablero[i*3+1] == tablero[i*3+2] != ' ':
            return tablero[i*3]
        # Columnas
        if tablero[i] == tablero[i+3] == tablero[i+6] != ' ':
            return tablero[i]  
    # Verificar diagonales
    if tablero[0] == tablero[4] == tablero[8] != ' ' or tablero[2] == tablero[4] == tablero[6] != ' ':
        return tablero[4]
    return None

def obtener_jugada_humana(tablero):
    """Obtiene y valida la jugada del jugador humano."""
    while True:
        try:
            pos = int(input("Elige una posición (1-9): ")) - 1
            if 0 <= pos <= 8 and tablero[pos] == ' ':
                return pos
            print("Posición inválida o ocupada. Intenta de nuevo.")
        except ValueError:
            print("Por favor ingresa un número del 1 al 9.")

def obtener_jugada_ia(tablero):
    """Determina la jugada de la IA."""
    movimientos_disponibles = [i for i, casilla in enumerate(tablero) if casilla == ' ']
    # Probar cada movimiento posible
    for simbolo in ['O', 'X']:  # Primero intenta ganar, luego bloquear
        for movimiento in movimientos_disponibles:
            tablero_prueba = tablero.copy()
            tablero_prueba[movimiento] = simbolo
            if hay_ganador(tablero_prueba) == simbolo:
                return movimiento
    # Si no hay jugadas decisivas, elige una posición aleatoria
    return random.choice(movimientos_disponibles)

def jugar():
    """Función principal que controla el flujo del juego."""
    tablero = [' ' for _ in range(9)]
    print("¡Bienvenido al Tres en Raya!")
    imprimir_tablero(tablero)
    while True:
        # Turno del jugador humano
        tablero[obtener_jugada_humana(tablero)] = 'X'
        imprimir_tablero(tablero)
        # Verificar si el juego terminó
        ganador = hay_ganador(tablero)
        if ganador:
            print(f"¡{'Ganaste' if ganador == 'X' else 'La IA ha ganado'}!")
            break
        if ' ' not in tablero:
            print("¡Empate!")
            break
        
        # Turno de la IA
        print("Turno de la IA...")
        tablero[obtener_jugada_ia(tablero)] = 'O'
        imprimir_tablero(tablero)
        
        # Verificar si el juego terminó
        ganador = hay_ganador(tablero)
        if ganador:
            print(f"¡{'Ganaste' if ganador == 'X' else 'La IA ha ganado'}!")
            break
        if ' ' not in tablero:
            print("¡Empate!")
            break

if __name__ == "__main__":
    jugar()