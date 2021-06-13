import pygame

from src.objects.object import Object
from src.sprites import sprites


class Ship(Object):
    def __init__(self, screen, speed):
        self.speed = speed
        self.screen = screen

        # Chama o super-construtor da classe Ship, que seria
        # o construtor da classe Object
        super().__init__(50, screen.get_height() / 2, 50, 50)

        self.sprite = pygame.transform.scale(sprites.red_ship_3, (int(self.size.x), int(self.size.y)))

    def move_up(self, dt):
        self.pos.y -= self.speed * dt

    def move_down(self, dt):
        self.pos.y += self.speed * dt

    def step(self):
        if self.pos.y < 0:
            self.pos.y = 0
        elif self.pos.y + self.size.y > self.screen.get_height():
            self.pos.y = self.screen.get_height() - self.size.y

    def draw(self):
        self.screen.blit(self.sprite, (self.pos.x, self.pos.y))
