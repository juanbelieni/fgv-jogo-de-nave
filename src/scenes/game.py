import pygame

from src.objects.background import Background
from src.objects.ship import Ship


class GameScene:
    def __init__(self, screen):
        self.screen = screen
        self.background = Background(self.screen)
        self.ship = Ship(screen, 300)

    def step(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.ship.move_up(dt)
        if keys[pygame.K_DOWN]:
            self.ship.move_down(dt)

        self.background.step(dt)
        self.ship.step()

    def draw(self):
        self.background.draw()
        self.ship.draw()
