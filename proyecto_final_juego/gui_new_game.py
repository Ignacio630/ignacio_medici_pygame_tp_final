import pygame

from config import *
from mapa import Mapa
from gui_menu import Menu

class New_game(Menu):

    def __init__(self, name, main_screen, x, y, w, h, path, image_name, active,level,delta_ms) -> None:
        super().__init__(name, main_screen, x, y, w, h, path, image_name, active)
        # self.setup_menu = setup_menu
        self.level = level
        self.delta_ms = delta_ms
    def update(self):
        if self.button_list["new_game"].is_active:
            self.level.run(self.delta_ms)
            self.active = False

    def draw(self):
        super().draw()  
        