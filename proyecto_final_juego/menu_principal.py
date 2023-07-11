# import pygame
# from gui_boton import Boton
# from funciones_utiles import *
# # from mapa import Mapa
# class Menu_princial():

#     def __init__(self,screen) -> None:
#         self.buttons_list = []
#         self.screen = screen
#         self.path_button = "{0}".format(PATH_MENU)
#         self.surface_menu = getSurface(path=self.path_button,frame=0,flag_flip=False,size=(ANCHO_MENU,ALTO_MENU))
#         self.rect_menu = self.surface_menu.get_rect(center=(ANCHO_PANTALLA/2,ALTO_PANTALLA/2))

#     def setup_form_menu(self,path_buttons):
#         for path in path_buttons:
#             button = Boton(path="{0}".format(PATH_MENU),size=(150,75),frame=path,master_screen=self.surface_menu,pos=(150,50))
#             self.buttons_list.append(button)
        
#     def update(self,event):
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             print(event.pos)
#         self.setup_form_menu(path_buttons=setup_main_menu)
        
#         self.buttons_list[0].draw()
#         # for button in self.buttons_list:
#         #     button.draw()
#     def draw(self,event):
#         self.update(event)
#         self.screen.blit(self.surface_menu,self.rect_menu)
#         if DEBUG:
#             pygame.draw.rect(self.screen,R,self.rect_menu,1)            