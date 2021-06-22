from random import randint

import pygame
from pygame import Vector2

from src.objects.object import Object
from src.sprites import sprites


class Enemy(Object):
    def __init__(self, screen, speed, what_enemy):
        self.screen = screen
        self.speed = speed
        self.what_enemy = what_enemy

        width, height = self.screen.get_size()

        super().__init__(width * 1.5, randint(20, height - 70), 50, 50)

        self.enemy_1 = pygame.transform.scale(sprites.enemy_1, (int(self.size.x), int(self.size.y)))
        self.enemy_2 = pygame.transform.scale(sprites.enemy_2, (int(self.size.x), int(self.size.y)))
        self.enemy_3 = pygame.transform.scale(sprites.enemy_3, (int(self.size.x), int(self.size.y)))
        self.enemy_4 = pygame.transform.scale(sprites.enemy_4, (int(self.size.x), int(self.size.y)))

    def update(self, dt):
        delta = Vector2(- self.speed * dt, 0)
        self.move_by(delta)

    def draw(self):
        if self.what_enemy == 1:
            self.screen.blit(self.enemy_1, (self.pos.x, self.pos.y))
        elif self.what_enemy == 2:
            self.screen.blit(self.enemy_2, (self.pos.x, self.pos.y))
        elif self.what_enemy == 3:
            self.screen.blit(self.enemy_3, (self.pos.x, self.pos.y))
        else: 
            self.screen.blit(self.enemy_4, (self.pos.x, self.pos.y))
