import pygame
from constantes import*

class Enemy:

    def __init__(self,size,pos) -> None:
        self.surface_enemy = pygame.surface.Surface((size,size))
        self.surface_enemy.fill(G)
        self.rect_enemy = self.surface_enemy.get_rect(topleft = pos)
        
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 3
        self.direction.x = self.speed
        self.direction.y = self.speed
    def enemy_movement_x(self,limits,world_speed):
        self.rect_enemy.x += world_speed + self.direction.x
        for limit in limits:
            if self.rect_enemy.colliderect(limit.rect):
                if self.direction.x > 0:
                    self.rect_enemy.right = limit.rect.left
                    self.direction.x = -self.speed
                elif self.direction.x < 0:
                    self.rect_enemy.left = limit.rect.right
                    self.direction.x = self.speed
                    
    def enemy_movement_y(self,limits,world_speed):
        self.rect_enemy.y += world_speed + self.direction.y
        for limit in limits:
            if self.rect_enemy.colliderect(limit.rect):
                if self.direction.y > 0:
                    self.rect_enemy.bottom = limit.rect.top
                    self.direction.y = -self.speed
                elif self.direction.y < 0:
                    self.rect_enemy.top = limit.rect.bottom
                    self.direction.y = self.speed

    def update(self,world_speed,limits,movimiento):
        if movimiento:
            self.enemy_movement_x(limits,world_speed)
        else:
            self.enemy_movement_y(limits,world_speed)


    def draw(self,screen):
        screen.blit(self.surface_enemy,self.rect_enemy)
        
        if DEBUG:
            pygame.draw.rect(screen,R,self.rect_enemy,1)