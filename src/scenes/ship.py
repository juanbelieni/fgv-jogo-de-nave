import pygame

from src.objects.object import Object
from src.sprites import sprites


class Ship(Object):
    def __init__(self, screen, speed): # recebe o objeto screen pra saber a altura maxima e minima que pode andar, mas ta feio
        self.speed = speed # velocidade float, serve de multiplicador no move
        _, height = screen.get_size() # pega o tamanho da tela, mas fica estranho, melhor fazer diferente
        self.screen_height = height
        self.screen = screen

        #self.ship = pygame.image.load(sprites.ship) # cria o sprite da nave
        #self.ship_rect = self.ship.get_rect() # cria o retangulo em que a nave ta

        # Chama o super-construtor da classe Ship, que seria
        # o construtor da classe Object
        super().__init__(50, height / 2, 50, 50) # aqui seta pos e size


    def move_up(self):
        self.pos.y -= 1 * self.speed

    def move_down(self):
        self.pos.y += 1 * self.speed

    def step(self):
        if self.pos.y < 0:
            self.pos.y = 0
        elif self.pos.y + self.size.y> self.screen_height:
            self.pos.y = self.screen_height - self.size.y

    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (self.pos.x, self.pos.y, self.size.x, self.size.y))

# metodo de mover pra cima
# metodo de mover pra baixo
# argumento que seta a velocidade

# verifica se a nave ta na tela
# desenha a nave