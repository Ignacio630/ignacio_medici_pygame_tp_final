import pygame 
from config import *
from funciones_utiles import *
from player import Player
from enemigo import Enemy
from plataformas import Plataforma
from bonfire import Bonfire

class Mapa:
    def __init__(self,level_design,screen,path_musica,volumen) -> None:
        self.platforms_list = []
        self.limits_list = []
        self.enemy_list = []
        self.bonfire_list = []
        self.musica_fondo = cargar_musica(path=path_musica,volumen=volumen,repetir=-1)
        self.music_playing = False
        self.screen = screen    
        self.world_move_x = 0
        self.setup_map(level_design)

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
                    self.player = Player(path=PATH_JUGADOR,speed_walk=SPEED_WALK,speed_run=SPEED_RUN,jump_power=-16,jump_height=200,gravity=0.8,size=(50,90),pos=(x,y))
                if row == "E":
                    enemy = Enemy(platform_size,(x,y))
                    self.enemy_list.append(enemy)
                if row == "F":
                    campfire = Bonfire(self.screen,(x,y),platform_size)
                    self.bonfire_list.append(campfire)

    def colliders_player_x(self,player):
        player.rect_jugador.x += player.direction_movement.x * player.speed_walk
        
        for platform in self.platforms_list:
            if platform.rect.colliderect(player.rect_jugador):
                if player.direction_movement.x < 0:
                    player.rect_jugador.left = platform.rect.right
                    player.direction_movement.x = 0
                elif player.direction_movement.x > 0:
                    player.rect_jugador.right = platform.rect.left
                    player.direction_movement.x = 0
    
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
            
    def player_camara(self,player,player_x,direction_x):
        if  direction_x < 0:
            self.world_move_x = 8
            player.walk_speed = 0
        elif direction_x > 0:
            self.world_move_x = -8
            player.walk_speed = 0
        else:
            self.world_move_x = 0
            player.walk_speed = 5

    def run(self,delta_ms):
        #fondo
        self.screen.fill(W)
        #mundo
        for platform in self.platforms_list:
            platform.update(self.world_move_x)
            platform.draw(self.screen)
            
        for limit in self.limits_list:
            limit.update(self.world_move_x)
            limit.draw(self.screen)

        for bonfire in self.bonfire_list:
            bonfire.update(self.player,self.world_move_x,delta_ms)
            bonfire.draw()

        
        for enemy in self.enemy_list:
            # enemy.enemy_movement(self.limits_list)
            enemy.update(self.world_move_x,self.limits_list,True)
            enemy.draw(self.screen)

        #jugador
        player = self.player
        self.player_camara(player,player.rect_jugador.x,player.direction_movement.x)
        self.player.update(delta_ms)
        self.player.hability_fireball.update(world_move_x=self.world_move_x)
        self.player.hability_fireball.draw(self.screen)
        self.colliders_player_x(self.player)
        self.colliders_player_y(self.player)
        self.player.draw(self.screen)
