import pygame
from constantes import *
from gui_menu import Menu
from gui_boton import Botton

class Main_menu(Menu):

    def __init__(self, name, main_screen, x, y, w, h, path, image_name, active,setup_menu) -> None:
        super().__init__(name, main_screen, x, y, w, h, path, image_name, active)
        self.button_list = []
        self.setup_buttons_form(setup_main_menu=setup_menu,path=path)

    def button_action(self,event_type):
        print(event_type)

    def setup_buttons_form(self,setup_main_menu,path):
        
        for button_name in setup_main_menu:
            if button_name == "title":
                button = Botton(main_screen=self.main_screen,w=360,h=100,x=self.x + ANCHO_MENU/5 ,y=50,path=path,image_name=button_name,event=self.button_action,event_type=None)
                self.button_list.append(button)
            if button_name == "new_game":
                button = Botton(main_screen=self.main_screen,w=300,h=75,x=self.x + ANCHO_MENU/4,y=200,path=path,image_name=button_name,event=self.button_action,event_type=None)
                self.button_list.append(button)
            if button_name == "load_game":
                button = Botton(main_screen=self.main_screen,w=300,h=75,x=self.x + ANCHO_MENU/4,y=300,path=path,image_name=button_name,event=self.button_action,event_type=None)
                self.button_list.append(button)
            if button_name == "options":
                button = Botton(main_screen=self.main_screen,w=300,h=75,x=self.x + ANCHO_MENU/4,y=400,path=path,image_name=button_name,event=self.button_action,event_type=None)
                self.button_list.append(button)
            if button_name == "exit":
                button = Botton(main_screen=self.main_screen,w=300,h=75,x=self.x + ANCHO_MENU/4,y=600,path=path,image_name=button_name,event=self.button_action,event_type=None)
                self.button_list.append(button)

    def update(self,event_list):
        for aux_botton in self.button_list:
            aux_botton.update(event_list)

    def draw(self,event_list):
        super().draw()
        self.update(event_list=event_list)
        for botton in self.button_list:
            botton.draw()