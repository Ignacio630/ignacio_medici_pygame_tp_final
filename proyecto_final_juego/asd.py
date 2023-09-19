import pygame
import sys

# Inicializa pygame
pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Línea Transparente")

# Color rojo sin transparencia
color_rojo = (255, 0, 0)

# Crea una superficie transparente
surface_transparente = pygame.Surface((400, 400), pygame.SRCALPHA)

# Cambia la transparencia de la superficie (50% de opacidad)
surface_transparente.set_alpha(0)

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpia la pantalla
    screen.fill((0, 0, 0))

    # Dibuja una línea en la superficie transparente
    pygame.draw.line(surface_transparente, color_rojo, (100, 100), (300, 300), 5)

    # Copia la superficie transparente en la pantalla
    screen.blit(surface_transparente, (0, 0))

    # Actualiza la pantalla
    pygame.display.flip()

# Salir del programa
pygame.quit()
sys.exit()