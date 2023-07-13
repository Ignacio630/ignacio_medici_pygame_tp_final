import pygame

from constantes import *
class Bonfire:

    def __init__(self,screen,pos,size) -> None:
        self.screen = screen
        self.surface = pygame.surface.Surface((size,size))
        self.surface.fill(R)
        self.rect = self.surface.get_rect(topleft=pos)
    

    def update(self,player,world_speed_x):
        keys = pygame.key.get_pressed()
        if player.rect_jugador.colliderect(self.rect):
            if keys[pygame.K_e]:
                player.hp = 100
                player.mana = 100
        self.rect.x += world_speed_x        

    def draw(self):

        self.screen.blit(self.surface,self.rect)