import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

class Planeta:
    def __init__(self, nombre, distancia, velocidad, color, tamaño):
        self.nombre = nombre
        self.distancia = distancia
        self.velocidad = velocidad
        self.color = color
        self.tamaño = tamaño
        self.angulo = 0
    
    def mover(self):
        self.angulo += self.velocidad
        x = self.distancia * np.cos(self.angulo)
        y = self.distancia * np.sin(self.angulo)
        return x, y


# Configuración inicial
fig, ax = plt.subplots(figsize=(4, 4))
ax.axis('off')  # Ocultamos los ejes para simplificar

# Crear el sol (punto fijo)
sol = plt.Circle((0, 0), 0.1, color='yellow', zorder=10)
ax.add_patch(sol)

# Crear planetas (nombre, distancia, velocidad, color, tamaño)
planetas = [
    Planeta("Mercurio", 0.2, 0.2, 'gray', 6),
    Planeta("Venus", 0.6, 0.18, 'orange', 8),
    Planeta("Tierra", 0.8, 0.15, 'blue', 15),
    Planeta("Marte", 1.0, 0.1, 'red', 7)
]

# Dibujar órbitas (círculos simples)
for planeta in planetas:
    orbita = plt.Circle((0, 0), planeta.distancia, color='lightgray', alpha=0.3)
    ax.add_patch(orbita)

# Crear puntos para los planetas
puntos = [ax.plot([], [], 'o', color=p.color, markersize=p.tamaño)[0] for p in planetas]

# Función de animación
def actualizar(frame):
    for i, planeta in enumerate(planetas):
        x, y = planeta.mover()
        puntos[i].set_data([x], [y])  # Wrap x and y in lists
    return puntos

# Crear la animación
ani = FuncAnimation(fig, actualizar, frames=500, interval=50)

plt.title("Sistema Solar Sencillo")
plt.show()