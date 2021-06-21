import pygame

from src.objects.background import Background
from src.scenes.scene import Scene
from src.sprites import sprites

# Game over font 
txt = 'Pressione ENTER para continuar...'
font = pygame.font.SysFont(pygame.font.get_default_font(), 30)


class GameOverScene(Scene):
    def __init__(self, screen):
        self.screen = screen
        self.background = Background(self.screen)

        width, height = self.screen.get_size()
        self.size_x, self.size_y = 400, 400
        self.X = width / 2 - self.size_x / 2
        self.Y = height / 2 - self.size_y / 2

        self.image = pygame.transform.scale(sprites.game_over, (self.size_x, self.size_y))
        self.over_text = font.render(txt, 1, (200, 60, 60))

    def draw(self):
        self.background.draw()
        s = pygame.Surface((1000, 600), pygame.SRCALPHA)
        s.fill((0, 0, 0, 100))  # valor de alpha sobre a cor
        self.screen.blit(s, (0, 0))
        self.screen.blit(self.image, (self.X - 20, self.Y))
        self.screen.blit(self.over_text, (315, 500))

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            self.emit("RESTART")

        self.background.update(dt)
