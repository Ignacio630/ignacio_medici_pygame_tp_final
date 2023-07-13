import pygame

class Campfire:

    def __init__(self,screen,pos,size) -> None:
        self.screen = screen
        self.surface = pygame.surface.Surface((size,size))
        self.rect = self.surface.get_rect(topleft=pos)
    

    def update(self,player,keys):

        if player.rect_jugador.colliderect(self.rect) and keys[pygame.K_e]:
            player.hp = 100
            player.mana = 100
            
    def draw(self):

        self.screen.blit(self.surface,self.rect)