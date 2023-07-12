import pygame

from funciones_utiles import *
from gui_boton import Button

class Menu:
    menu_names = {}
    def __init__(self,name,main_screen,x,y,w,h,path,image_name,is_active) -> None:
        self.menu_names[name] = self
        self.button_list = []
        self.main_screen = main_screen
        self.surface_menu = getSurface(path=path,frame=image_name,flag_flip=False,size=(w,h))
        self.rect_menu = self.surface_menu.get_rect(topleft =(x,y))
        self.is_active = is_active
        self.x = x
        self.y = y
    
    def set_active(self,name):
        for aux_menu in self.menu_names:
            aux_menu.is_active = False
        self.menu_names[name].is_active = True
    def draw(self):
        self.main_screen.blit(self.surface_menu,self.rect_menu)
