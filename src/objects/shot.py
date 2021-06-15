import pygame
from pygame import Vector2

from src.objects.object import Object
from src.sprites import sprites

SHOT_SIZE = Vector2(15, 15)


class Shot(Object):
    def __init__(self, screen, initial_pos, speed):
        self.speed = speed
        self.screen = screen

        super().__init__(initial_pos.x, initial_pos.y, SHOT_SIZE.x, SHOT_SIZE.y)
        self.sprite = pygame.transform.scale(sprites.shot_3, (int(SHOT_SIZE.x), int(SHOT_SIZE.y)))

    def update(self, dt):
        delta = Vector2(self.speed * dt, 0)
        self.move_by(delta)

    def draw(self):
        self.screen.blit(self.sprite, (self.pos.x, self.pos.y))