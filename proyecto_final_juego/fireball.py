import pygame

from funciones_utiles import * 

class Fireball:    
    def __init__(self,path,pos,size,frame,direction=True) -> None:
        if direction:
            self.animation = getSurfaceFromSeparateSprite(path=path,frames=frame,flag_flip=False,size=size)
        else:
            self.animation = getSurfaceFromSeparateSprite(path=path,frames=frame,flag_flip=True,size=size)
        
        self.frame = 0
        self.pos = pos
        self.image_fireball = self.animation[self.frame]
        self.rect = self.image_fireball.get_rect(topleft=self.pos)
        self.speed_fireball = 0
        self.current_time = 0

    def fire(self,speed):
        self.speed_fireball = speed


    def update(self,world_move,delta_ms):    
        self.rect.x += world_move.x + self.speed_fireball
        self.current_time += delta_ms
        if (self.current_time >= 200):
            self.current_time = 0
            if(self.frame < len(self.animation)-1):
                self.frame += 1
            else:
                self.frame = 0

    def draw(self,screen):
        screen.blit(self.image_fireball,self.rect)
        if DEBUG:
            pygame.draw.rect(screen,R,self.rect,1)