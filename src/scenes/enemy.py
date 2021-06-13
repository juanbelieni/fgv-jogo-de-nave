import pygame

from src.objects.object import Object
from src.sprites import sprites


class Bolso(Object):
    def __init__(self, screen, speed): # recebe o objeto screen pra saber a altura maxima e minima que pode andar, mas ta feio
        self.speed = speed # velocidade float, serve de multiplicador no move
        _, height = screen.get_size() # pega o tamanho da tela, mas fica estranho, melhor fazer diferente
        self.screen_height = height
        self.screen = screen
        super().__init__(60, height / 2, 30, 30)# sáida dos inimigos
        def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 0), (self.pos.x, self.pos.y, self.size.x, self.size.y))