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

platform_size = 52



#definimos las dimensiones iniciales de la pantalla
# ANCHO_PANTALLA = 1920
# ALTO_PANTALLA = 1080

#JUGADOR

VIDA_JUGADOR = 100
MANA_JUGADOR = 100

ANCHO_JUGADOR = 70
ALTO_JUGADOR = 110

SPEED_WALK = 4
SPEED_RUN = 6

#pantalla
RESOLUTION_WIDTH = 1200
RESOLUTION_HEIGHT = len(level_map_1) * 52
# #Menu
MENU_WIDTH = 400
MENU_HEIGHT = RESOLUTION_HEIGHT

#setup menu
SETUP_MAIN_MENU = ["title","load_game","options","exit"]
SETUP_OPTIONS_MENU = ["sonido","volver"]
SETUP_LEVELS_MENU = ["level_1","level_2","level_3","exit"]