import pygame
from funciones_utiles import *

class Botton():

    def __init__(self, main_screen, w, h, x, y,path,image_name,event,event_type) -> None:
        self.main_screen = main_screen
        self.subscreen = getSurface(path=path,frame=image_name,flag_flip=False,size=(w,h))
        self.subscreen_rect = self.subscreen.get_rect(topleft=(x,y))
        self.main_rect = self.main_screen.get_rect()
        self.event = event
        self.event_type = event_type
        
    def setup_button(self):
        self.subscreen_rect_collider = pygame.Rect(self.subscreen_rect)
        self.subscreen_rect_collider.x += self.main_rect.x
        self.subscreen_rect_collider.y += self.main_rect.y

    def update(self,event_list):
        self.setup_button()
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:                
                if self.subscreen_rect_collider.collidepoint(event.pos):
                    print(self.subscreen_rect)
                    self.event(self.event_type)

    def draw(self):
        self.main_screen.blit(self.subscreen,self.subscreen_rect)
        if DEBUG:
            pygame.draw.rect(self.main_screen,(255,0,0),self.subscreen_rect,1)