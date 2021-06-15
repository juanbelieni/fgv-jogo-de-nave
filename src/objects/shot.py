import pygame
from pygame import Vector2

from src.objects.object import Object

SHOT_SIZE = Vector2(10, 10)


class Shot(Object):
    def __init__(self, screen, initial_pos, speed):
        self.speed = speed
        self.screen = screen

        super().__init__(initial_pos.x, initial_pos.y, SHOT_SIZE.x, SHOT_SIZE.y)

    def update(self, dt):
        delta = Vector2(self.speed * dt, 0)
        self.move_by(delta)
        

    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (self.pos.x, self.pos.y, self.size.x, self.size.y))
