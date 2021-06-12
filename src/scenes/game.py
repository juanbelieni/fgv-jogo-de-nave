from src.objects.background import Background
from src.scenes.ship import Ship
import pygame

class GameScene:
    def __init__(self, screen):
        self.screen = screen
        self.background = Background(self.screen)
        self.ship = Ship(screen, 2)

    def step(self, events):
        keys = pygame.key.get_pressed()  #checking pressed keys
        if keys[pygame.K_UP]:
            self.ship.move_up()
        if keys[pygame.K_DOWN]:
            self.ship.move_down()


        self.background.step()
        self.ship.step()

    def draw(self):
        self.background.draw()
        self.ship.draw()
