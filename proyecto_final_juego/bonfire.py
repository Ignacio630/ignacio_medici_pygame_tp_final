import pygame

from funciones_utiles import *

class Bonfire:

    def __init__(self,screen,pos,size) -> None:
        self.bonfire = getSurfaceFromSeparateSprite("{0}".format(PATH_BONFIRE),7,False,(size,size))
        self.screen = screen

        self.frame = 0
        self.animation = self.bonfire
        self.surface = self.animation[self.frame]
        self.rect = self.surface.get_rect(topleft=pos)
        self.current_time = 0

    def update(self,player,world_speed_x,delta_ms):
        self.current_time += delta_ms
        self.rect.x += world_speed_x  
        keys = pygame.key.get_pressed()

        if player.rect_jugador.colliderect(self.rect):
            if keys[pygame.K_e]:
                player.hp = 100
                player.mana = 100
        if self.current_time >= 200:
            if(self.frame < len(self.animation)-1):
                self.frame += 1
            else:
                self.frame = 0

    def draw(self):
        self.screen.blit(self.surface,self.rect)