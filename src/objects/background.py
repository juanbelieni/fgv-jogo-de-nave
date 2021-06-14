import pygame
from pygame import Vector2

from src.objects.object import Object
from src.sprites import sprites


class Background(Object):
    def __init__(self, screen):
        self.screen = screen
        width, height = self.screen.get_size()

        # Chama o super-construtor da classe Background, que seria
        # o construtor da classe Object
        super().__init__(0, 0, width, height)

        # Reajusta o tamanho do sprite do background, para que tenha o mesmo tamanho da tela
        self.sprite = pygame.transform.scale(sprites.background, (width, height))

    def update(self, dt):
        delta = Vector2(-0.25 * self.size.x * dt, 0)
        self.move_by(delta)

        if self.pos.x < -self.size.x:
            pos = Vector2(0, 0)
            self.move_to(pos)

    def draw(self):
        self.screen.blit(self.sprite, (self.pos.x, self.pos.y))
        self.screen.blit(self.sprite, (self.pos.x + self.size.x, self.pos.y))
