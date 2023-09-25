import pygame
from config import*

class Enemy:

    def __init__(self,path,size,pos,frames) -> None:
        self.surface_enemy = pygame.surface.Surface((size,size))
        self.surface_enemy.fill(R)
        self.rect_enemy = self.surface_enemy.get_rect(topleft = pos)
        
        self.hp = VIDA_ENEMIGO
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 3
        self.direction.x = self.speed
        self.direction.y = self.speed
        self.is_dead = False

    def stat_bar(self,screen,x,y,color,stat):
        widht = self.surface_enemy.get_width()
        height = self.surface_enemy.get_height()

        stat_calc = int((stat / VIDA_ENEMIGO) * widht)
        
        rect_borde = pygame.Rect(x,y,widht,height/4)
        rect_stat = pygame.Rect(x,y,stat_calc,height/4)
        
        pygame.draw.rect(screen,color,rect_stat)
        pygame.draw.rect(screen,BLACK,rect_borde,2)

    def enemy_movement_x(self,limits,world_speed):
        self.rect_enemy.x += world_speed.x + self.direction.x

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

    def enemy_attack(self,screen):
        pygame.draw.line(screen,R,(self.rect_enemy.x,100),(self.rect_enemy.x,200))

    def kill(self):
        if self.hp <= 0:
            self.is_dead = True

    def update(self,world_speed,limits,movimiento):
        if movimiento:
            self.enemy_movement_x(limits,world_speed)
        else:
            self.enemy_movement_y(limits,world_speed)

        self.kill()

    def draw(self,screen):
        if not self.is_dead:
            screen.blit(self.surface_enemy,self.rect_enemy)
            self.stat_bar(screen=screen,x=self.rect_enemy.x,y=self.rect_enemy.y-25,color=G,stat=self.hp)
            self.enemy_attack(screen)
        if DEBUG:
            pygame.draw.rect(screen,R,self.rect_enemy,1)