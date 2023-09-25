import pygame
from levels import *
#fotogramas por segundo del juego
FPS = 60

#debug
DEBUG = True

#definimos la direccion de la carpeta con los recursos

PATH_RECURSOS = "proyecto_final_juego/recursos"
PATH_MENU = "{0}/menu/".format(PATH_RECURSOS)
PATH_SPRITES = "{0}/sprites/".format(PATH_RECURSOS)
PATH_ENEMIGO = "{0}enemigo/".format(PATH_SPRITES)
PATH_JUGADOR = "{0}jugador/".format(PATH_SPRITES)
PATH_STAND = "stand/"
PATH_WALK = "walk/"
PATH_RUN = "run/"
PATH_JUMP = "jump/"
PATH_ATTACK = "attack/"
PATH_SHOOT = "shoot/"
PATH_FIREBALL = "fireball/"
PATH_FONDO = "{0}/fondo/".format(PATH_RECURSOS)
PATH_TERRENO = "{0}terreno/".format(PATH_FONDO)
PATH_BONFIRE = "{0}bonfire/".format(PATH_FONDO)
PATH_AGUA = "{0}agua/".format(PATH_FONDO)
PATH_PLATAFORMA = "{0}plataforma/".format(PATH_FONDO)
PATH_MUSICA = "{0}/musica/".format(PATH_RECURSOS)
#colores

R = (255,0,0)
G = (0,255,0)
B = (0,0,255)
BLACK = (0,0,0)
W = (255,255,255)
T = (0, 0, 0, 0)

#direccion
DIRECCION = True

#Opciones resolucion
resolution = 2

if resolution == 0:
    JUMP_POWER = 14
    
    platform_size = 83
    
    RESOLUTION_WIDTH = 1920
    RESOLUTION_HEIGHT = len(level_map_1) * platform_size

    ANCHO_JUGADOR = 50 * (RESOLUTION_WIDTH / RESOLUTION_HEIGHT)
    ALTO_JUGADOR = 90 * (RESOLUTION_WIDTH / RESOLUTION_HEIGHT)

    
elif resolution == 1:
    platform_size = 69

    JUMP_POWER = 13
    
    RESOLUTION_WIDTH = 1600
    RESOLUTION_HEIGHT = len(level_map_1) * platform_size

    ANCHO_JUGADOR = 40 * (RESOLUTION_WIDTH / RESOLUTION_HEIGHT)
    ALTO_JUGADOR = 80 * (RESOLUTION_WIDTH / RESOLUTION_HEIGHT)

elif resolution == 2: 
    platform_size = 59
    
    JUMP_POWER = 12
    
    RESOLUTION_WIDTH = 1366
    RESOLUTION_HEIGHT = len(level_map_1) * platform_size
    
    ANCHO_JUGADOR = 40 * (RESOLUTION_WIDTH / RESOLUTION_HEIGHT)
    ALTO_JUGADOR = 70 * (RESOLUTION_WIDTH / RESOLUTION_HEIGHT)

else: 
    platform_size = 59

    JUMP_POWER = 12
    
    RESOLUTION_WIDTH = 1366
    RESOLUTION_HEIGHT = len(level_map_1) * platform_size

    ANCHO_JUGADOR = 40 * (RESOLUTION_WIDTH / RESOLUTION_HEIGHT)
    ALTO_JUGADOR = 70 * (RESOLUTION_WIDTH / RESOLUTION_HEIGHT)


#definimos las dimensiones iniciales de la pantalla
# ANCHO_PANTALLA = 1920
# ALTO_PANTALLA = 1080

#JUGADOR
dificultad = 0

if dificultad == 0:
    #Jugador
    VIDA_JUGADOR = 100
    MANA_JUGADOR = 100
    #Enemigo
    VIDA_ENEMIGO = 200
elif dificultad == 1:
    #Jugador
    VIDA_JUGADOR = 75
    MANA_JUGADOR = 70
    #Enemigo
    VIDA_ENEMIGO = 300



SPEED_WALK = 4
SPEED_RUN = 6

#Plataformas



# #Menu
MENU_WIDTH = 400
MENU_HEIGHT = RESOLUTION_HEIGHT

#setup menu
SETUP_MAIN_MENU = ["title","load_game","options","exit"]
SETUP_OPTIONS_MENU = ["sonido","volver"]
SETUP_LEVELS_MENU = ["level_1","level_2","level_3","exit"]