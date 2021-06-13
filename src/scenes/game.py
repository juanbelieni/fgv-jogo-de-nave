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
        if keys[pygame.K_SPACE] and (len(self.shots) == 0 or self.shots[-1].pos.x > 400):
            self.shots.append(Shot(self.ship, shot_speed, self.screen))

        self.background.step(dt)
        self.ship.step()

        for shot in self.shots:
            if shot.pos.x > self.screen.get_width():
                del shot # não usei OO do shot porque nao consegui expluir o elemento da lista, mudar isso
            else:
                shot.move_right(dt)

    def draw(self):
        self.background.draw()
        for shot in self.shots:
            shot.draw()
        self.ship.draw()
        
