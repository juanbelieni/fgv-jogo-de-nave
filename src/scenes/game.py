from src.objects.background import Background


class GameScene:
    def __init__(self, screen):
        self.screen = screen
        self.background = Background(self.screen)

    def step(self):
        self.background.step()

    def draw(self):
        self.background.draw()
