import pygame

from funciones_utiles import *
from gui_widget import Widget
from gui_boton import Botton

class Menu:
    menu_names = {}
    def __init__(self,name,main_screen,x,y,w,h,path,image_name,active) -> None:
        self.menu_names[name] = self
        self.button_list = []
        self.main_screen = main_screen
        self.surface_menu = getSurface(path=path,frame=image_name,flag_flip=False,size=(w,h))
        self.rect_menu = self.surface_menu.get_rect(topleft =(x,y))
        self.active = active
        self.x = x
        self.y = y
        

    
    def draw(self):
        self.main_screen.blit(self.surface_menu,self.rect_menu)
