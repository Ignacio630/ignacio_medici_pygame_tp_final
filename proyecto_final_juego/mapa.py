import pygame 
import time 
from config import *
from funciones_utiles import *
from player import Player
from enemigo import Enemy
from plataformas import Plataforma
from bonfire import Bonfire
from score import Score



class Mapa:
    def __init__(self,level_design,screen,path_musica,volumen,path_fondo) -> None:
        self.platforms_list = []
        self.limits_list = []
        self.enemy_list = []
        self.bonfire_list = []
        self.background_list = getSurfaceFromSeparateSprite(path=path_fondo,frames=5,flag_flip=False,size=(1000,RESOLUTION_HEIGHT))
        self.musica_fondo = cargar_musica(path=path_musica,volumen=volumen,repetir=-1)
        self.music_playing = False
        self.screen = screen    
        self.world_move = pygame.math.Vector2()
        self.speed_background = 0.5
        self.scroll = 0
        self.setup_map(level_design)
        self.bg_rect = self.background_list[0].get_rect()
        #
        self.font = pygame.font.Font(None,15)
        #
        self.start_time = time.time()
        self.time = 0
        self.score = Score("Souls:",(RESOLUTION_WIDTH-125,0),(260,50))
        self.font_time = pygame.font.Font(None, 30)
        self.time_surface = self.font_time.render("Time: " + self.formatted_time(), True, W)
        self.time_rect = self.time_surface.get_rect(topright=(RESOLUTION_WIDTH - 10, 30))
        #
    
    def update_time(self):
        current_time = time.time()
        self.time = current_time - self.start_time
    
    def formatted_time(self):
        min = int(self.time // 60)
        seg = int(self.time % 60)
        return "{0:02}:{1:02}".format(min,seg)
    def draw_time(self):
        self.update_time()
        self.screen.blit(self.time_surface, self.time_rect)

    def draw_background(self):
        bg_width = self.background_list[0].get_width()
        
        for x in range(len(self.background_list)):
            self.speed_background = 1
            for bg in self.background_list[0:4]:
                self.screen.blit(bg,((bg_width * x) - self.scroll * self.speed_background ,0))
                self.speed_background += 0.2
                
    def setup_map(self,level_map):

        for column_index,column in enumerate(level_map):
            for row_index,row in enumerate(column):
                x = row_index * platform_size
                y = column_index * platform_size
                if row == "C":
                    plataforma = Plataforma((x,y),platform_size,path="{0}".format(PATH_TERRENO),flag=True,frame=0)
                    self.platforms_list.append(plataforma)
                if row == "D":
                    plataforma = Plataforma((x,y),platform_size,path="{0}".format(PATH_TERRENO),flag=True,frame=2)
                    self.platforms_list.append(plataforma)
                if row == "I":
                    plataforma = Plataforma((x,y),platform_size,path="{0}".format(PATH_TERRENO),flag=True,frame=1)
                    self.platforms_list.append(plataforma)
                if row == "T":
                    plataforma = Plataforma((x,y),platform_size,path="{0}".format(PATH_TERRENO),flag=True,frame=4)
                    self.platforms_list.append(plataforma)
                if row == "L":
                    plataforma = Plataforma((x,y),platform_size,path="{0}".format(PATH_PLATAFORMA),flag=True,frame=15)
                    self.limits_list.append(plataforma)
                if row == "P":
                    self.player = Player(path=PATH_JUGADOR,speed_walk=SPEED_WALK,speed_run=SPEED_RUN,jump_power=-16,jump_height=200,gravity=0.8,size=(ANCHO_JUGADOR,ALTO_JUGADOR),pos=(x,y))
                if row == "E":
                    enemy = Enemy(platform_size,(x,y))
                    self.enemy_list.append(enemy)
                if row == "F":
                    campfire = Bonfire(self.screen,(x,y),platform_size)
                    self.bonfire_list.append(campfire)

    def colliders_player_x(self,direction_movement_x,player_rect):
        for platform in self.platforms_list:
            if platform.rect.colliderect(player_rect):
                if direction_movement_x < 0 :
                    player_rect.left = platform.rect.right
                    direction_movement_x = 0
                elif direction_movement_x > 0:
                    player_rect.right = platform.rect.left
                    direction_movement_x = 0

    def music_is_playing(self,volumen):
        if volumen == 0:
            self.music_playing = False
        else: 
            self.music_playing = True
            
    def colliders_player_y(self,player):
        player = self.player
        player.apply_gravity()

        for platform in self.platforms_list:
            if platform.rect.colliderect(player.rect_jugador):
                if player.direction_movement.y < 0:
                    player.rect_jugador.top = platform.rect.bottom
                    player.direction_movement.y = 0
                elif player.direction_movement.y > 0:
                    player.rect_jugador.bottom = platform.rect.top                
                    player.direction_movement.y = 0

    def update_enemy(self):
        for enemy in self.enemy_list:
            if enemy.is_dead:
                self.enemy_list.remove(enemy)
                self.score.add_score(10)
            else:
                enemy.update(self.world_move,self.limits_list,True)
                enemy.draw(self.screen)
                if enemy.rect_enemy.colliderect(self.player.rect_melee_attack):
                    enemy.is_dead = True

    def run(self,delta_ms,keys):
        #fondo
        self.draw_background()
        if keys[pygame.K_LEFT] and self.world_move.x > 0:
            self.scroll -= SPEED_WALK / 2
        elif keys[pygame.K_RIGHT]and self.world_move.x < 0:
            self.scroll += SPEED_WALK / 2
        #mundo
        for platform in self.platforms_list:
            platform.update(self.world_move)
            platform.draw(self.screen)
            
        for limit in self.limits_list:
            limit.update(self.world_move)
            limit.draw(self.screen)

        for bonfire in self.bonfire_list:
            bonfire.update(self.player,self.world_move,delta_ms)
            bonfire.draw()

        self.update_enemy()

        #jugador
        self.score.draw(self.screen)
        player = self.player
        player.update(delta_ms)

        self.colliders_player_x(player.direction_movement.x,player.rect_jugador)
        self.colliders_player_y(player)

        player.draw(self.screen)
        player.map_actions(self.world_move)

        self.time_surface = self.font_time.render("Time: " + self.formatted_time(), True, W)
        self.time_rect = self.time_surface.get_rect(topright=(RESOLUTION_WIDTH - 10, 30))

        # Dibujar el tiempo en la pantalla
        self.draw_time()
