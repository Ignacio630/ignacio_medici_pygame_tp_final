import pygame
from config import *
from gui_menu import Menu
from gui_main_menu import Main_menu
from gui_boton import Button
from levels import * 
class Options(Menu):

    def __init__(self, name, main_screen, x, y, w, h, path, image_name, active,setup_menu) -> None:
        super().__init__(name, main_screen, x, y, w, h, path, image_name, active)
        self.button_dict = {}
        self.setup_menu = setup_menu
        self.master_screen = pygame.display.get_surface()
        self.setup_buttons_form(path=path)
        
    def button_action(self,button):
        if button == "volver":
            if self.button_dict[button].is_active:
                self.is_active = False
                
    def setup_buttons_form(self,path):
        for button_name in self.setup_menu:
            if button_name == "sonido":
                button = Button(main_screen=self.main_screen,w=260,h=50,x=(RESOLUTION_WIDTH/2)-130,y=350,path=path,image_name="sonido",action=self.button_action,name=button_name)
                self.button_dict[button_name] = button
            if button_name == "volver":
                button = Button(main_screen=self.main_screen,w=260,h=50,x=(RESOLUTION_WIDTH/2)-130,y=RESOLUTION_HEIGHT-200,path=path,image_name="exit",action=self.button_action,name=button_name)
                self.button_dict[button_name] = button

    

    def update(self,event_list):
        for aux_button in self.setup_menu:
            self.button_dict[aux_button].update(event_list)

        

    def draw(self,event_list):
        super().draw()
        self.update(event_list=event_list)
        for button in self.setup_menu:
            self.button_dict[button].draw()
