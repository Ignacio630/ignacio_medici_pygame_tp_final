import pygame
from config import * 
from funciones_utiles import *

class Plataforma:

    def __init__(self,pos,size,path,flag,frame) -> None:
        self.surface = getSurface(path=path,frame=frame,flag_flip=flag,size=(size,size))
        self.rect = self.surface.get_rect(topleft = pos)

    def update(self,world_speed):
        self.rect.x += world_speed.x

    def draw(self,screen):
        screen.blit(self.surface,self.rect)
        if DEBUG:
            pygame.draw.rect(screen,R,self.rect,1)