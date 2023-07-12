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
PATH_FONDO = "{0}/fondo/".format(PATH_RECURSOS)
PATH_TERRENO = "{0}terreno/".format(PATH_FONDO)
PATH_AGUA = "{0}agua/".format(PATH_FONDO)
PATH_PLATAFORMA = "{0}plataforma/".format(PATH_FONDO)
#colores

R = (255,0,0)
G = (0,255,0)
B = (0,0,255)
B = (0,0,0)
W = (255,255,255)

#direccion

DIRECCION = True
DEBUG = True

platform_size = 52


level_map = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'X                            X',
    'X                            X',
    'X                            X',
    'X                            X',
    'X                            X',
    'X                            X',
    'X                            X',
    'X                            X',
    'X          L   E    L        X',
    'X           PPPPPPPP         X',
    'X                            X',
    'X    P                       X',
    'ICCCCCCCCCCCCCCCCCCCCCCCCCCCCD',
    'ITTTTTTTTTTTTTTTTTTTTTTTTTTTTD'

]

#definimos las dimensiones iniciales de la pantalla
ANCHO_PANTALLA = 1200
ALTO_PANTALLA = len(level_map) * platform_size
#form map
#Menu
ANCHO_MENU = ANCHO_PANTALLA/2
ALTO_MENU = ALTO_PANTALLA

SETUP_MAIN_MENU = ["title","new_game","load_game","options","exit"]

#JUGADOR

ANCHO_JUGADOR = 0
ALTO_JUGADOR = 0

SPEED_WALK = 4
SPEED_RUN = SPEED_WALK * 1.20 

