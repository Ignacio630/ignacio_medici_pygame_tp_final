import pygame
from funciones_utiles import *
pygame.init()

clock = pygame.time.Clock()
fps= 60

width = 800
height = 432

screen = pygame.display.set_mode((width,height))

run = True

surface = getSurfaceFromSeparateSprite(path="{0}background/".format(PATH_FONDO),frames=5,flag_flip=False,size=(700,height))
surface_width = surface[0].get_width()

scroll = 0
def draw_bg(surface):
    for x in range(5):
        speed = 1
        for bg in surface:
            screen.blit(bg,((x* surface_width) - scroll * speed,0))
            speed += 0.2
while run: 

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        scroll -= 1
    elif keys[pygame.K_RIGHT]:
        scroll += 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw_bg(surface=surface)
    pygame.display.update()


pygame.quit()