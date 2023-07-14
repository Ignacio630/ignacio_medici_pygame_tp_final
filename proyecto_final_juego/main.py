import pygame
from config import *
from levels import *
from gui_main_menu import Main_menu
from gui_options_menu import Options
from gui_load_level import LoadLevel
from mapa import Mapa

pantalla = pygame.display.set_mode((RESOLUTION_WIDTH, RESOLUTION_HEIGHT))
pygame.init()

tiempo = pygame.time.Clock()
esta_corriendo = True

main_menu = Main_menu(name="main_menu", main_screen=pantalla, x=RESOLUTION_WIDTH/4, y=0, w=MENU_WIDTH, h=MENU_HEIGHT ,path=PATH_MENU, image_name="0", active=True, setup_menu=SETUP_MAIN_MENU)
options = Options(name="options", main_screen=pantalla, x=RESOLUTION_WIDTH/4, y=0, w=MENU_WIDTH, h=MENU_HEIGHT ,path=PATH_MENU, image_name="0", active=False, setup_menu=SETUP_OPTIONS_MENU)
load_level = LoadLevel(name="load_level", main_screen=pantalla, x=RESOLUTION_WIDTH/4, y=0, w=MENU_WIDTH, h=MENU_HEIGHT ,path=PATH_MENU, image_name="0", active=False, setup_menu=SETUP_LEVELS_MENU)

mapa_1 = Mapa(level_map_1, pantalla, "{0}fondo/level_1_music.mp3".format(PATH_MUSICA), volumen=0.05)
mapa_2 = Mapa(level_map_2, pantalla, "{0}fondo/level_1_music.mp3".format(PATH_MUSICA), volumen=0.05)
mapa_3 = Mapa(level_map_3, pantalla, "{0}fondo/level_1_music.mp3".format(PATH_MUSICA), volumen=0.05)

menu_actual = main_menu

# bucle principal
while esta_corriendo:
    delta_ms = tiempo.tick(FPS)  
    event_list = pygame.event.get()
    for event in event_list: 
        if event.type == pygame.QUIT or main_menu.button_dict["exit"].is_active:
            esta_corriendo = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if isinstance(menu_actual, Options):
                    menu_actual = main_menu
                elif isinstance(menu_actual, Main_menu):
                    menu_actual = options

    if isinstance(menu_actual, Main_menu):
        main_menu.draw(event_list=event_list)
        if main_menu.button_dict["options"].is_active:
            menu_actual = options
        elif main_menu.button_dict["load_game"].is_active:
            menu_actual = load_level
    elif isinstance(menu_actual, Options):
        options.draw(event_list=event_list)
        if options.button_dict["volver"].is_active:
            menu_actual = main_menu
    elif isinstance(menu_actual, LoadLevel):
        load_level.draw(event_list=event_list)
        if load_level.button_dict["level_1"].is_active:
            menu_actual = mapa_1
        elif load_level.button_dict["level_2"].is_active:
            menu_actual = mapa_2
        elif load_level.button_dict["level_3"].is_active:
            menu_actual = mapa_3
    if isinstance(menu_actual, Mapa):
        menu_actual.run(delta_ms)

    pygame.display.flip()
    
pygame.quit()