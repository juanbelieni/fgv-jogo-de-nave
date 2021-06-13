from pygame import Vector2
import pygame.sprite


class Object:
    def __init__(self, x, y, width, height):
        self.pos = Vector2(x, y)
        self.size = Vector2(width, height)

    def collides_with(self, other):
        pass
    def move(self, delta) -> None:
        pass
