import pygame
from constantes import *

def getSurfaceFromSeparateSprite(path:str,frames:int,flag_flip:bool,size:tuple):
    lista_frames = []   

    for frame in range(0,frames):
        surface_sprite = pygame.image.load("{0}{1}.png".format(path,frame))
        surface_sprite = pygame.transform.scale(surface_sprite,size)
        if flag_flip:
            surface_sprite = pygame.transform.flip(surface_sprite,True,False)
        lista_frames.append(surface_sprite)
    return lista_frames

def getSurface(path:str,frame:int,flag_flip:bool,size:tuple):
    surface_sprite = pygame.image.load("{0}{1}.png".format(path,frame))
    surface_sprite = pygame.transform.scale(surface_sprite,size)
    if flag_flip:
        surface_sprite = pygame.transform.flip(surface_sprite,True,False)
    return surface_sprite

def getSurfaceFromSprites(path:str,columnas:int,filas:int,step:int,flag_flip:bool,size:tuple):
    lista_frames = []
    surface_sprite = pygame.image.load(path)
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