from random import randint

import pygame
from pygame import Vector2

from src.objects.object import Object
from src.sprites import sprites


class Enemy(Object):
    def __init__(self, screen, speed):
        self.screen = screen
        self.speed = speed

        width, height = self.screen.get_size()

        super().__init__(width * 1.5, randint(20, height - 70), 50, 50)

        self.sprite = pygame.transform.scale(sprites.red_ship_3, (int(self.size.x), int(self.size.y)))

    def update(self, dt):
        delta = Vector2(- self.speed * dt, 0)
        self.move_by(delta)

    def draw(self):
        self.screen.blit(self.sprite, (self.pos.x, self.pos.y))
