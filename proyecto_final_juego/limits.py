import pygame
from config import *

class Limits:

    def __init__(self,size,pos,screen) -> None:
        self.surface = pygame.surface.Surface((size,size))
        self.rect = self.surface.get_rect(topleft=pos)
        self.screen = screen
    
    def draw(self):
        self.screen.blit(self.surface,self.rect)