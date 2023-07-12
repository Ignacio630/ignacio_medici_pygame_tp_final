import pygame
from constantes import *
from gui_menu import Menu
from gui_new_game import New_game
from gui_boton import Button

class Main_menu(Menu):

    def __init__(self, name, main_screen, x, y, w, h, path, image_name, active,setup_menu) -> None:
        super().__init__(name, main_screen, x, y, w, h, path, image_name, active)
        self.button_dict = {}
        self.setup_menu = setup_menu
        self.setup_buttons_form(path=path)

    def button_action(self,button):
        print(f"hola{self.button_dict[button]}")
            
    def setup_buttons_form(self,path):
        for button_name in self.setup_menu:
            if button_name == "title":
                button = Button(main_screen=self.main_screen,w=360,h=100,x=self.x + ANCHO_MENU/5 ,y=50,path=path,image_name=button_name,action=self.button_action,action_param="",name=button_name)
                self.button_dict[button_name] = button
            if button_name == "new_game":
                button = Button(main_screen=self.main_screen,w=300,h=75,x=self.x + ANCHO_MENU/4,y=200,path=path,image_name=button_name,action=self.button_action,action_param="",name=button_name)
                self.button_dict[button_name] = button
            if button_name == "load_game":
                button = Button(main_screen=self.main_screen,w=300,h=75,x=self.x + ANCHO_MENU/4,y=300,path=path,image_name=button_name,action=self.button_action,action_param="",name=button_name)
                self.button_dict[button_name] = button
            if button_name == "options":
                button = Button(main_screen=self.main_screen,w=300,h=75,x=self.x + ANCHO_MENU/4,y=400,path=path,image_name=button_name,action=self.button_action,action_param="",name=button_name)
                self.button_dict[button_name] = button
            if button_name == "exit":
                button = Button(main_screen=self.main_screen,w=300,h=75,x=self.x + ANCHO_MENU/4,y=600,path=path,image_name=button_name,action=self.button_action,action_param="",name=button_name)
                self.button_dict[button_name] = button

    def update(self,event_list):
        for aux_button in self.setup_menu:
            self.button_dict[aux_button].update(event_list)
            self.button_action(aux_button)
    def draw(self,event_list):
        super().draw()
        self.update(event_list=event_list)
        for button in self.setup_menu:
            self.button_dict[button].draw()