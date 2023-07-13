import pygame
from constantes import *
from gui_main_menu import Main_menu
from mapa import Mapa

pantalla = pygame.display.set_mode((DICT_RESOLUTION_WIDHT["1280"],DICT_RESOLUTION_HEIGHT["720"]))

pygame.init()

tiempo = pygame.time.Clock()
esta_corriendo = True

def event(event_type):
    print(event_type)

main_menu = Main_menu(name="main_menu",main_screen=pantalla,x=DICT_RESOLUTION_WIDHT["1280"]/4,y=0,w=DICT_MENU_WIDHT["640"],h=DICT_MENU_HEIGHT["720"],path=PATH_MENU,image_name="0",active=True,setup_menu=SETUP_MAIN_MENU)

mapa_1 = Mapa(level_map,pantalla)

# bucle principal
while esta_corriendo:
    delta_ms = tiempo.tick(FPS)  
    keys = pygame.key.get_pressed() 
    event_list = pygame.event.get()
    for event in event_list: 
        if event.type == pygame.QUIT or main_menu.button_dict["exit"].is_active:
            esta_corriendo = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
        elif keys[pygame.K_ESCAPE]:
            main_menu.is_active = True

    #Update jugador, enemigo, mapa, etc

    if main_menu.is_active:
        main_menu.draw(event_list)
    else:
        mapa_1.run(delta_ms)
        
    pygame.display.flip()
    
pygame.quit()   