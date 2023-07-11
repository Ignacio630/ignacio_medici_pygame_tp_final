import pygame 
from constantes import * 
from jugador import Jugador
from enemigo import Enemy
from plataformas import Plataforma
from menu_principal import Menu_princial
from gui_boton import Boton
class Mapa:
    def __init__(self,level_design,screen) -> None:
        self.platforms_list = []
        self.limits_list = []
        self.enemy_list = []
        self.screen = screen    
        self.setup_map(level_design)
        self.world_move_x = 0
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
                    plataforma = Plataforma((x,y),platform_size,path="{0}".format(PATH_TERRENO),flag=True,frame=1)
                    self.limits_list.append(plataforma)
                if row == "P":
                    self.player = Jugador(path=PATH_JUGADOR,speed_walk=SPEED_WALK,speed_run=SPEED_RUN,jump_power=-16,jump_height=200,gravity=0.8,size=(50,90),pos=(x,y))
                if row == "E":
                    enemy = Enemy(platform_size,(x,y))
                    self.enemy_list.append(enemy)
                    

    def colliders_player_x(self,player):
        player.rect_jugador.x += player.direction_movement.x
        
        for platform in self.platforms_list:
            if platform.rect.colliderect(player.rect_jugador):
                if player.direction_movement.x < 0:
                    player.rect_jugador.left = platform.rect.right
                    player.direction_movement.x = 0
                elif player.direction_movement.x > 0:
                    player.rect_jugador.right = platform.rect.left
                    player.direction_movement.x = 0
                    
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
            
    def player_camara(self,player):
        if player.direction_movement.x < 0:
            self.world_move_x = SPEED_WALK
            player.walk_speed = 0
        elif player.direction_movement.x > 0:
            self.world_move_x = -SPEED_WALK
            player.walk_speed = 0
        else:
            self.world_move_x = 0
            player.walk_speed = SPEED_WALK

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
            
        for enemy in self.enemy_list:
            # enemy.enemy_movement(self.limits_list)
            enemy.update(self.world_move_x,self.limits_list,True)
            enemy.draw(self.screen)

        #jugador
        self.player_camara(self.player)
        self.player.update(delta_ms)
        self.colliders_player_x(self.player)
        self.colliders_player_y(self.player)
        self.player.draw(self.screen)
