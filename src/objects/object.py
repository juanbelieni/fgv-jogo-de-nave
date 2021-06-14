from pygame import Vector2
import pygame.sprite


class Object:
    def __init__(self, x, y, width, height):
        self.pos = Vector2(x, y)
        self.size = Vector2(width, height)

    def collides_with(self, other):
        si = self.pos
        sf = self.pos + self.size
        oi = other.pos
        of = other.pos + other.size

        if si[1] > of[1] or sf[1] < oi[1] or si[0] > of[0] or sf[0] < oi[0]:
            return False
        return True

    def move(self, delta) -> None:
        self.pos = self.pos + delta