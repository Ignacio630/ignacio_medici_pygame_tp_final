import pygame


screen = pygame.display.set_mode((800,800))
# Define la velocidad del objeto
objeto = pygame.rect.Rect(10,10,10,10)
objeto.fill((255,0,0))
OBJECT_SPEED = 10

# Obtiene el tiempo actual en milisegundos
current_time = pygame.time.get_ticks()
pygame.init()
# Bucle de eventos principal
while True:

    # Obtiene el siguiente evento de la cola de eventos
    event = pygame.event.poll()

    # Si el evento es un evento de cierre de ventana
    if event.type == pygame.QUIT:

        # Cierra la ventana y sale del bucle de eventos
        pygame.quit()
        sys.exit()

    # Calcula el tiempo transcurrido desde la última vez que se movió el objeto
    elapsed_time = pygame.time.get_ticks() - current_time

    # Si han pasado más de 100 milisegundos desde la última vez que se movió el objeto
    if elapsed_time >= 100:

        # Mueve el objeto 10 píxeles a la derecha
        objeto.x += OBJECT_SPEED
        screen.blit(screen,objeto)

        # Actualiza el tiempo actual
        current_time = pygame.time.get_ticks()

    # Renderiza la pantalla
    pygame.display.flip()
