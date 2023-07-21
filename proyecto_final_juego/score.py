import pygame

from config import *

class Score:
    def __init__(self, action, text, step_score, step_remove_score, pos_text):
        self.score = 0
        self.step_score = step_score
        self.step_remove_score = step_remove_score
        self.font_text = pygame.font.Font(None, 40)
        self.font_score = pygame.font.Font(None, 35)
        self.text_surface = self.font_score.render(text, True, B)
        self.text_rect = self.text_surface.get_rect(topleft=pos_text)
        self.pos_score = (self.text_rect.right + 10, self.text_rect.y)
        self.surface_score = self.font_score.render("{0}".format(self.score), True, B)

    def add_score(self):
        start_score = self.score
        score = self.score + self.step_score
        while start_score != score:    
            self.score += 1

    def remove_score(self):
        self.score -= self.step_score

    def update(self):
        self.add_score()
        self.remove_score()

    def draw(self, screen):
        self.update()
        self.surface_score = self.font_score.render("{0}".format(self.score), True, B)  # Update the score surface
        screen.blit(self.score_bg,self.rect_bg_score)
        screen.blit(self.text_surface, self.text_rect)
        screen.blit(self.surface_score, self.pos_score)