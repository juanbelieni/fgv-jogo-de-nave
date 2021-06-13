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
        self.pos.x -= self.size.x * dt * 0.2

        if self.pos.x < -self.size.x:
            # TODO: utilizar o método move, quando estiver implementado
            self.pos.x = 0

    def draw(self):
        self.screen.blit(self.sprite, (self.pos.x, self.pos.y))
        self.screen.blit(self.sprite, (self.pos.x + self.size.x, self.pos.y))
