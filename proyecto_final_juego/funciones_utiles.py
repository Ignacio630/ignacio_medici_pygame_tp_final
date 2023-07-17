import pygame
from config import *

def getSurfaceFromSeparateSprite(path:str,frames:int,flag_flip:bool,size:tuple):
    lista_frames = []   

    for frame in range(0,frames):
        surface_sprite = pygame.image.load("{0}{1}.png".format(path,frame)).convert_alpha()
        surface_sprite = pygame.transform.scale(surface_sprite,size)
        if flag_flip:
            surface_sprite = pygame.transform.flip(surface_sprite,True,False)
        lista_frames.append(surface_sprite)
    return lista_frames

def getSurface(path:str,frame:int,flag_flip:bool,size:tuple):
    surface_sprite = pygame.image.load("{0}{1}.png".format(path,frame)).convert_alpha()
    surface_sprite = pygame.transform.scale(surface_sprite,size)
    if flag_flip:
        surface_sprite = pygame.transform.flip(surface_sprite,True,False)
    return surface_sprite

def getSurfaceFromSprites(path:str,columnas:int,filas:int,step:int,flag_flip:bool,size:tuple):
    lista_frames = []
    surface_sprite = pygame.image.load(path).convert_alpha()
    surface_sprite = pygame.transform.scale(surface_sprite,size)
    ancho_frame = (surface_sprite.get_width()/columnas)
    alto_frame = (surface_sprite.get_height()/filas)

    for fila in range(filas):
        for columna in range(0,columnas,step):
            x = columna*ancho_frame
            y = fila*alto_frame
            surface_frame = surface_sprite.subsurface(x,y,ancho_frame,alto_frame)
            if(flag_flip):
                surface_frame = pygame.transform.flip(surface_frame,True,False)
            lista_frames.append(surface_frame)
    return lista_frames


def cargar_musica(path: str, volumen: float, repetir: int) -> None:
    '''
    Descripcion: Carga la musica del juego

    Parametros:
        path: ruta de la musica
        volumen: volumen de la musica
        repetir: numero de veces que se repite la musica

    Retorno: None
    '''

    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(volumen)
    pygame.mixer.music.play(repetir)

def apagar_musica():
    pygame.mixer.music.stop()

def cargar_sonido(path: str, volumen: float) -> None:
    '''
    Descripcion: Carga los sonidos del juego

    Parametros:
        path: ruta del sonido
        volumen: volumen del sonido

    Retorno: None
    '''
    sonido = pygame.mixer.Sound(path)
    sonido.set_volume(volumen)
    sonido.play()