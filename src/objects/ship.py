import pygame

from src.objects.object import Object
from src.sprites import sprites


class Ship(Object):
    def __init__(self, screen, speed):
        self.screen = screen
        self.speed = speed

        # Chama o super-construtor da classe Ship, que seria
        # o construtor da classe Object
        super().__init__(50, screen.get_height() / 2, 50, 50)

        self.sprite = pygame.transform.scale(sprites.red_ship_3, (int(self.size.x), int(self.size.y)))

    def move_up(self, dt):
        delta = pygame.Vector2(0, -self.speed * dt)
        self.move_by(delta)

    def move_down(self, dt):
        delta = pygame.Vector2(0, +self.speed * dt)
        self.move_by(delta)

    def draw(self):
        self.screen.blit(self.sprite, (self.pos.x, self.pos.y))
