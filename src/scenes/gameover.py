import pygame

from src.objects.background import Background
from src.scenes.scene import Scene
from src.sprites import sprites

class GameOverScene(Scene):
    def __init__(self, screen):
        self.screen = screen
        self.background = Background(self.screen)
        self.font_name = 'src/Fonte_do_game.TTF'
        
        width, height = self.screen.get_size()
        self.size_x, self.size_y = 400, 400
        self.X = width / 2 - self.size_x / 2
        self.Y = height / 2 - self.size_y / 2

        self.image = pygame.transform.scale(sprites.game_over, (self.size_x, self.size_y))

    def draw(self):
        self.background.draw()
        s = pygame.Surface((1000, 600), pygame.SRCALPHA)
        s.fill((0, 0, 0, 150))  # valor de alpha sobre a cor
        self.screen.blit(s, (0, 0))
        self.screen.blit(self.image, (self.X - 20, self.Y))
        self.draw_text("Pressione ENTER para continuar", 20, 480, 500)
        
    def update(self, dt, _):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            self.emit("RESTART")

        self.background.update(dt)

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, (100, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.screen.blit(text_surface,text_rect)
