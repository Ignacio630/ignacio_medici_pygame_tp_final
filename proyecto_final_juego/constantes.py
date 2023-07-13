#fotogramas por segundo del juego
FPS = 60   

#debug
DEBUG = True

#definimos la direccion de la carpeta con los recursos

PATH_RECURSOS = "recursos"
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
PATH_FONDO = "{0}/fondo/".format(PATH_RECURSOS)
PATH_TERRENO = "{0}terreno/".format(PATH_FONDO)
PATH_AGUA = "{0}agua/".format(PATH_FONDO)
PATH_PLATAFORMA = "{0}plataforma/".format(PATH_FONDO)
#colores

R = (255,0,0)
G = (0,255,0)
B = (0,0,255)
BLACK = (0,0,0)
W = (255,255,255)

#direccion

DIRECCION = True
DEBUG = True

platform_size = 52


level_map = [
    'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC',
    'C                                                  C',
    'C                                                  C',
    'C                                                  C',
    'C                                                  C',
    'C                                                  C',
    'C                                                  C',
    'C                                                  C',
    'C          L   E    L                              C',
    'C           PPPPPPPP                               C',
    'C                                                  C',
    'C    P         F                                   C',
    'ICCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCD',
    'ITTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTD',
    'ITTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTD'
]
#definimos las dimensiones iniciales de la pantalla
# ANCHO_PANTALLA = 1920
# ALTO_PANTALLA = 1080

DICT_RESOLUTION_WIDHT = {"1920":1920,"1280":1280,"1024":1024,"800":800}
DICT_RESOLUTION_HEIGHT = {"1080":1080,"720":720,"768":768,"600":600}

# #Menu
DICT_MENU_WIDHT = {"960":960,"640":640,"512":512,"400":400}
DICT_MENU_HEIGHT = {"1080":1080,"720":720,"768":768,"600":600}

#setup menu
SETUP_MAIN_MENU = ["title","new_game","load_game","options","exit"]

#JUGADOR

ANCHO_JUGADOR = 0
ALTO_JUGADOR = 0

SPEED_WALK = 4
SPEED_RUN = SPEED_WALK * 1.20 

