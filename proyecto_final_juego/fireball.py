import pygame

from funciones_utiles import * 

class Fireball:    
    def __init__(self,path,pos,size,frame) -> None:
        self.animation = getSurfaceFromSeparateSprite(path=path,frames=frame,flag_flip=False,size=size)
        self.frame = 0
        self.pos = pos
        self.image_fireball = self.animation[self.frame]
        self.rect = self.image_fireball.get_rect(topleft=self.pos)
        self.speed_fireball = 0

    def fire(self,speed):
        self.speed_fireball = speed

    def collition(self):
        if (self.rect.x < 0 or self.rect.x > RESOLUTION_WIDTH):
            self.rect.topleft = self.pos
            self.speed_fireball = 0


    def update(self,world_move):    
        self.rect.x += world_move.x + self.speed_fireball
        # if (self.tiempo_transcurrido >= 200):
        #     self.tiempo_transcurrido = 0
        if(self.frame < len(self.animation)-1):
            self.frame += 1
        else:
            self.frame = 0
        self.collition()
    def draw(self,screen):
        screen.blit(self.image_fireball,self.rect)
        if DEBUG:
            pygame.draw.rect(screen,R,self.rect,1)