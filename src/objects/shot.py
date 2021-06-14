import pygame

from src.objects.object import Object
from src.sprites import sprites

class Shot(Object):
    def __init__(self, ship, speed, screen):
        self.speed = speed
        self.screen = screen

        super().__init__(ship.pos.x, ship.pos.y, 50, 50)

    def move_right(self, dt):
        delta = pygame.Vector2(self.speed*dt,0)
        self.move(delta)

    def remove(self):
        if self.pos.x > self.screen.get_width():
            return True

        #Futuramente podemos inserir a lista de inimigos como parâmetro
        # for enemy in list_enemies:
        #   if self.colides_with(enemy):
        #       return True
        return False

    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (self.pos.x, self.pos.y, 10, 10))