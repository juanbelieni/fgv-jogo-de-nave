import pygame
from pygame.constants import KEYDOWN

from src.objects.background import Background
from src.objects.ship import Ship
from src.objects.shot import Shot

class GameScene:
    def __init__(self, screen):
        self.screen = screen
        self.background = Background(self.screen)
        self.ship = Ship(screen, 300)
        self.shots = []

    def step(self, dt):
        keys = pygame.key.get_pressed()
        shot_speed = 400

        if keys[pygame.K_UP]:
            self.ship.move_up(dt)
        if keys[pygame.K_DOWN]:
            self.ship.move_down(dt)
        if keys[pygame.K_SPACE] and len(self.shots) == 0 or keys[pygame.K_SPACE] and self.shots[-1].pos.x > 400:
            self.shots.append(Shot(self.ship, shot_speed, self.screen))

        self.background.step(dt)
        self.ship.step()

        if len(self.shots) != 0 and self.shots[0].pos.x > self.screen.get_width():
            self.shots.pop(0) # não usei OO do shot porque nao consegui expluir o elemento da lista, mudar isso
        for i in range(len(self.shots)):
            self.shots[i].move(dt)

    def draw(self):
        self.background.draw()
        self.ship.draw()
        for shot in self.shots:
            shot.draw()
