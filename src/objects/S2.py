from random import randint

import pygame
from pygame import Vector2

from src.objects.object import Object
from src.sprites import sprites


class S2(Object):
    def __init__(self, screen):
        self.screen = screen
        self.S2 = pygame.transform.scale(sprites.shot_3, (50, 50))

        super().__init__(0, 0, 100, 100)

    def draw(self, counter):
        self.screen.blit(self.S2, (self.pos.x + 100*counter, self.pos.y))
