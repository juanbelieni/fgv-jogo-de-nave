# desenhar o tiro
# mover o tiro
#mover para o lado
import pygame

from src.objects.object import Object
from src.sprites import sprites

#cor, velocidade, 
class Shot(Object):
    def __init__(self,screen, speed): # 
    
        self.speed = speed # v
        _, height = screen.get_size() # 
        self.screen_height = height
        self.screen = screen

        
        super().__init__(ship, 10, 10) # saida do tiro


    def move_right(self):
        self.pos.x += 3 * self.speed


    def step(self):
        if self.pos.x < 0:
            self.pos.x = 0
        elif self.pos.x + self.size.x> self.screen_height:
            self.pos.x = self.screen_height - self.size.x

    def draw(self):
        pygame.draw.rect(self.screen, (60, 60, 60), (self.pos.x, self.pos.y, self.size.x, self.size.y))