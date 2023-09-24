import pygame
from config import *
from levels import *
from gui_main_menu import Main_menu
from gui_options_menu import Options
from gui_load_level import LoadLevel
from mapa import Mapa

pantalla = pygame.display.set_mode((RESOLUTION_WIDTH, RESOLUTION_HEIGHT))
pygame.display.set_caption("Souls like")
pygame.init()

tiempo = pygame.time.Clock()
esta_corriendo = True

main_menu = Main_menu(name="main_menu", main_screen=pantalla, x=RESOLUTION_WIDTH/4, y=0, w=MENU_WIDTH, h=MENU_HEIGHT ,path=PATH_MENU, image_name="0", active=True, setup_menu=SETUP_MAIN_MENU)
options = Options(name="options", main_screen=pantalla, x=RESOLUTION_WIDTH/4, y=0, w=MENU_WIDTH, h=MENU_HEIGHT ,path=PATH_MENU, image_name="0", active=False, setup_menu=SETUP_OPTIONS_MENU)
load_level = LoadLevel(name="load_level", main_screen=pantalla, x=RESOLUTION_WIDTH/4, y=0, w=MENU_WIDTH, h=MENU_HEIGHT ,path=PATH_MENU, image_name="0", active=False, setup_menu=SETUP_LEVELS_MENU)

mapa_1 = Mapa(level_map_1, pantalla, "{0}fondo/level_1_music.mp3".format(PATH_MUSICA), volumen=0.05,path_fondo="{0}background/".format(PATH_FONDO))
mapa_2 = Mapa(level_map_2, pantalla, "{0}fondo/level_1_music.mp3".format(PATH_MUSICA), volumen=0.05,path_fondo="{0}background/".format(PATH_FONDO))
mapa_3 = Mapa(level_map_3, pantalla, "{0}fondo/level_1_music.mp3".format(PATH_MUSICA), volumen=0.05,path_fondo="{0}background/".format(PATH_FONDO))
   
menu_actual = main_menu

# bucle principal
while esta_corriendo:
    delta_ms = tiempo.tick(FPS)
    event_list = pygame.event.get()
    keys = pygame.key.get_pressed()
    for event in event_list: 
        if event.type == pygame.QUIT or main_menu.button_dict["exit"].is_active or keys[pygame.K_ESCAPE]:
            esta_corriendo = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
    
    mapa_1.run(delta_ms=delta_ms,keys=keys)
    pygame.display.update()
    
pygame.quit()