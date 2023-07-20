import pygame

from config import *

class Score:
    def __init__(self, action, text, step_score, step_remove_score, pos_text) -> None:
        self.score = 0
        self.action = action
        self.font_text = pygame.font.Font(None,20)
        self.font_score = pygame.font.Font(None,15)
        self.text_surface = self.font_score.render(text=text,antialias=True,color=B)
        self.text_rect = self.text_surface.getrect(pos_text)
        self.pos_score =  (self.text_rect.x + 40, self.text_rect.y)
        self.surface_score = self.font_score.render(self.score,True,B)
        self.step_score = step_score
        self.step_remove_score = step_remove_score
    


    def add_score(self):
        if self.action:
            self.score += self.step_score
        else:
            self.score -= self.step_remove_socre

    def update(self):
        pass

    def draw(self,screen):
        screen.blit(self.text_surface,self.text_rect)