import pygame
from config import *
from levels import *
from funciones_utiles import *
from fireball import Fireball

class Player:
    def __init__(self,path,speed_walk,speed_run,jump_power,jump_height,gravity,size,pos,screen) -> None:
        self.stay_frames_r = getSurfaceFromSeparateSprite("{0}{1}".format(path,PATH_STAND),9,False,size)
        self.stay_frames_l = getSurfaceFromSeparateSprite("{0}{1}".format(path,PATH_STAND),9,True,size)
        self.walk_frame_r = getSurfaceFromSeparateSprite("{0}{1}".format(path,PATH_WALK),6,False,size)
        self.walk_frame_l = getSurfaceFromSeparateSprite("{0}{1}".format(path,PATH_WALK),6,True,size)
        self.run_frame_r = getSurfaceFromSeparateSprite("{0}{1}".format(path,PATH_RUN),8,False,size)
        self.run_frame_l = getSurfaceFromSeparateSprite("{0}{1}".format(path,PATH_RUN),8,True,size)
        self.attack_frame_r = getSurfaceFromSeparateSprite("{0}{1}".format(path,PATH_ATTACK),2,False,(ANCHO_JUGADOR*1.5,ALTO_JUGADOR))
        self.attack_frame_l = getSurfaceFromSeparateSprite("{0}{1}".format(path,PATH_ATTACK),2,True,(ANCHO_JUGADOR*1.5,ALTO_JUGADOR))
        #
        self.screen = screen
        self.frame = 0
        self.animation = self.stay_frames_r
        self.size_player = size
        self.imagen_jugador = self.animation[self.frame]
        self.rect_jugador = self.imagen_jugador.get_rect(topright = pos)
        #
        self.fireballs = []
        self.rect_melee_attack = pygame.rect.Rect(0,0,0,0)
        self.rect_collition = pygame.rect.Rect(0,0,0,0)
        #
        self.direction = DIRECCION
        self.direction_movement = pygame.math.Vector2()
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.jump_power = jump_power
        self.jump_height = jump_height
        self.start_jump = 0
        #
        self.is_grounded = False 
        self.is_jumping = False
        self.is_attacking = False
        self.is_shooting = False
        self.gravity = gravity
        self.tiempo_transcurrido = 0
        #
        self.hp = VIDA_JUGADOR
        self.mana = MANA_JUGADOR
        self.score = 0
        
    def melee_attack(self,pantalla):    
        if self.direction:
            x, y = self.rect_jugador.topright
            self.animation = self.attack_frame_r
            self.rect_melee_attack = pygame.draw.rect(surface=pantalla,color=T,rect=(x,y,ANCHO_JUGADOR/2,ALTO_JUGADOR))
        else:
            x, y = self.rect_jugador.topleft
            self.animation = self.attack_frame_l
            self.rect_melee_attack = pygame.draw.rect(surface=pantalla,color=T,rect=(x,y,ANCHO_JUGADOR/2,ALTO_JUGADOR))
          
    def collition_line(self):
        pass

    def range_attack(self):
        if self.mana >= 10:
            if self.direction:
                self.mana -= 10
                self.fireballs.append(Fireball("{0}{1}".format(PATH_JUGADOR,PATH_FIREBALL),self.rect_jugador.midleft,(50,25),7,self.direction))
                for fireball in self.fireballs:
                    fireball.fire(10) 
            else:
                self.mana -= 10
                self.fireballs.append(Fireball("{0}{1}".format(PATH_JUGADOR,PATH_FIREBALL),self.rect_jugador.midleft,(50,25),7,self.direction))
                for fireball in self.fireballs:
                    fireball.fire(-10)  
        else:
            print("mana insuficiente")
    # HUD
    def stat_bar(self,screen,x,y,color,stat):
        widht = 300
        height = 20
        stat_calc = int((stat / 100)* widht)
        rect_borde = pygame.Rect(x,y,widht,height)
        rect_stat = pygame.Rect(x,y,stat_calc,height)
        pygame.draw.rect(screen,color,rect_stat)
        pygame.draw.rect(screen,BLACK,rect_borde,3)
    #quieto
    def stay(self):
        if self.direction:
            self.animation = self.stay_frames_r
        else:
            self.animation = self.stay_frames_l
    #caminar izq-der
    def walk(self):
        if self.direction:
            self.direction_movement.x = 1
            self.animation = self.walk_frame_r
        elif not self.direction:
            self.direction_movement.x = -1
            self.animation = self.walk_frame_l
    #correr
    def run(self):
        if self.direction:
            self.direction_movement.x = 1
            self.animation = self.run_frame_r
        else:
            self.direction_movement.x = -1
            self.animation = self.run_frame_l
    #saltar
    def jump(self):
        if self.direction_movement.y == 0:
            self.direction_movement.y = self.jump_power
            self.is_jumping = True
        else:
            self.is_jumping = False

    def inputs(self):
        keys = pygame.key.get_pressed()
        self.stay()
        self.direction_movement.x = 0
        
        if keys[pygame.K_SPACE] == 1 and not self.is_jumping:
            self.jump()
        if keys[pygame.K_SPACE] == 0 and self.is_jumping:
            self.is_jumping = False
            
        if keys[pygame.K_RIGHT]:
            self.direction = True
            self.walk()
        
        if keys[pygame.K_LEFT]:
            self.direction = False
            self.walk()
        
        if keys[pygame.K_RIGHT] and keys[pygame.K_LSHIFT]: 
            self.direction = True
            self.run()

        if keys[pygame.K_LEFT] and keys[pygame.K_LSHIFT]:
            self.direction = False
            self.run()
        
        #Shoot attack
        if keys[pygame.K_x] == 1 and not self.is_shooting:
            self.range_attack()
            self.is_shooting = True
        if keys[pygame.K_x] == 0 and self.is_shooting:
            self.is_shooting = False

        #Melee attack
        if keys[pygame.K_z] == 1 and not self.is_attacking:
            self.melee_attack(self.screen)
            self.is_attacking = True
        if keys[pygame.K_z] == 0 and self.is_attacking:
            self.is_attacking = False
        
    def apply_gravity(self):
        self.direction_movement.y += self.gravity
        self.rect_jugador.y += self.direction_movement.y
        
    def update(self,delta_ms):         
        #Aplicar animacion
        self.inputs()
        self.tiempo_transcurrido += delta_ms
        if (self.tiempo_transcurrido >= 500):
            self.tiempo_transcurrido = 0
            if(self.frame < len(self.animation)-1):
                self.frame += 1
            else:
                self.frame = 0
        
        self.rect_jugador.x += self.direction_movement.x * self.speed_walk

    def map_actions(self, world_move):
        if self.direction_movement.x < 0 and self.rect_jugador.x < RESOLUTION_WIDTH / 3:
            world_move.x = 6
            self.speed_walk = 0
            self.speed_run = 0

        elif self.direction_movement.x > 0 and self.rect_jugador.x > RESOLUTION_WIDTH - (RESOLUTION_WIDTH / 2):
            world_move.x = -6
            self.speed_walk = 0
            self.speed_run = 0
            
        else:
            world_move.x = 0
            self.speed_walk = SPEED_WALK
            self.speed_run = SPEED_RUN

    def draw(self):
        if self.frame < len(self.animation):
            self.imagen_jugador = self.animation[self.frame]
        else:
            self.frame = 0

        self.screen.blit(self.imagen_jugador,self.rect_jugador)
        
        self.stat_bar(screen=self.screen,x=25,y=25,color=G,stat=self.hp)
        self.stat_bar(screen=self.screen,x=25,y=50,color=B,stat=self.mana)


        if DEBUG:
            pygame.draw.rect(self.screen,R,self.rect_jugador,1)                                                                           