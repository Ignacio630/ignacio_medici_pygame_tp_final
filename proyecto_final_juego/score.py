import pygame
from config import *

class Score:
    def __init__(self, text, pos_text,bg_size):
        self.score = 0
        self.font_text = pygame.font.Font(None, 40)
        self.font_score = pygame.font.Font(None, 35)
        self.text_surface = self.font_score.render(text, True, B)
        self.text_rect = self.text_surface.get_rect(topleft=pos_text)
        self.pos_score = (self.text_rect.right + 10, self.text_rect.y)
        self.surface_score = self.font_score.render("{0}".format(self.score), True, B)
        self.bg_surface = pygame.surface.Surface(bg_size)
        self.bg_rect = self.bg_surface.get_rect(topleft=pos_text)
    def add_score(self, points=0):
        self.score += points

    def remove_score(self,points=0):
        self.score -= points

    def update(self):
        self.surface_score = self.font_score.render("{0}".format(self.score), True, B)

    def draw(self, screen):
        self.update()
        screen.blit(self.bg_surface,self.bg_rect)
        screen.blit(self.text_surface, self.text_rect)
        screen.blit(self.surface_score, self.pos_score)
