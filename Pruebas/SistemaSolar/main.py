import pygame
import math
import random

# Inicializar pygame
pygame.init()
# Configuración
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sistema Solar POO")

# Colores
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
WHITE = (255, 255, 255)

class CuerpoCeleste:
    def __init__(self, nombre, x, y, radio, color):
        self.nombre = nombre
        self.x = x
        self.y = y
        self.radio = radio
        self.color = color
        self.angulo = 0
        self.velocidad = 0
        self.distancia = 0
    
    def dibujar(self, pantalla):
        pygame.draw.circle(pantalla, self.color, (self.x, self.y), self.radio)
    
    def mover(self):
        # Método base que será sobrescrito (polimorfismo)
        pass
 

class Estrella(CuerpoCeleste):
    def __init__(self, nombre, x, y):
        super().__init__(nombre, x, y, 30, YELLOW)
    
    def mover(self):
        # Las estrellas no se mueven (en nuestro modelo simplificado)
        pass

class Planeta(CuerpoCeleste):
    def __init__(self, nombre, x, y, color, radio=10, velocidad=0.01, distancia=100):
        super().__init__(nombre, x, y, radio, color)
        self.velocidad = velocidad
        self.distancia = distancia
        self.angulo = random.uniform(0, 2 * math.pi)
    
    def mover(self):
        # Movimiento circular alrededor del centro
        self.angulo += self.velocidad
        self.x = WIDTH // 2 + math.cos(self.angulo) * self.distancia
        self.y = HEIGHT // 2 + math.sin(self.angulo) * self.distancia

class PlanetaConLuna(Planeta):
    def __init__(self, nombre, x, y, color, radio=15, velocidad=0.01, distancia=250):
        super().__init__(nombre, x, y, color, radio, velocidad, distancia)
        self.lunas = []
    
    def agregar_luna(self, luna):
        self.lunas.append(luna)
    
    def dibujar(self, pantalla):
        super().dibujar(pantalla)
        for luna in self.lunas:
            luna.dibujar(pantalla)
    
    def mover(self):
        super().mover()
        for luna in self.lunas:
            luna.mover(self.x, self.y)

class Luna(CuerpoCeleste):
    def __init__(self, nombre, planeta_x, planeta_y, color):
        distancia = 30  # Distancia al planeta
        super().__init__(nombre, planeta_x + distancia, planeta_y + distancia, 5, color)
        self.distancia = distancia
        self.angulo = random.uniform(0, 2 * math.pi)
        self.velocidad = 0.05
    
    def mover(self, planeta_x, planeta_y):
        self.angulo += self.velocidad
        self.x = planeta_x + math.cos(self.angulo) * self.distancia
        self.y = planeta_y + math.sin(self.angulo) * self.distancia

def main():
    run = True
    clock = pygame.time.Clock()
    
    # Crear sistema solar
    sol = Estrella("Sol", WIDTH // 2, HEIGHT // 2)
    tierra = Planeta("Tierra", 0, 0, BLUE, 12, 0.02, 150)
    marte = Planeta("Marte", 0, 0, (255, 100, 100), 10, 0.015, 200)
    jupiter = PlanetaConLuna("Júpiter", 0, 0, (255, 200, 150))
    
    # Agregar lunas a Júpiter
    luna1 = Luna("Ío", jupiter.x, jupiter.y, WHITE)
    jupiter.agregar_luna(luna1)
    
    cuerpos = [sol, tierra, marte, jupiter]
    
    while run:
        clock.tick(60)
        background_image = pygame.image.load("fondo.png").convert()
        background_rect= background_image.get_rect()
        screen.blit(background_image, background_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # Mover y dibujar todos los cuerpos celestes
        for cuerpo in cuerpos:
            cuerpo.mover()
            cuerpo.dibujar(screen)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()