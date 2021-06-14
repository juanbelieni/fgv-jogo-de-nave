import pygame

from src.objects.object import Object
from src.sprites import sprites


class Background(Object):
    def __init__(self, screen):
        self.screen = screen
        width, height = self.screen.get_size()

        # Chama o super-construtor da classe Background, que seria
        # o construtor da classe Object
        super().__init__(0, 0, width, height)

        # Reajusta o tamanho do sprite do background, para que tenha o mesmo tamanho da tela
        self.sprite = pygame.transform.scale(sprites.background, (width, height))

    def step(self, dt):
        delta = pygame.Vector2(-0.2*self.size.x*dt,0)
        self.move(delta)

        if self.pos.x < -self.size.x:
            delta[0] = self.size.x
            self.move(delta)

    def draw(self):
        self.screen.blit(self.sprite, (self.pos.x, self.pos.y))
        self.screen.blit(self.sprite, (self.pos.x + self.size.x, self.pos.y))
