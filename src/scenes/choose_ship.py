import pygame
from pygame import Vector2

from src.objects.background import Background
from src.scenes.scene import Scene
from src.sprites import sprites

font = pygame.font.SysFont(pygame.font.get_default_font(), 30)

SHIP_SIZE = Vector2(100, 100)

game_configs = {
    "resistant": {
        "lives": 5,
        "shoot_distance": 269.21,
        "velocity": 350,
        "description": "Nave mais resistente, com 2 vidas extras",
        "sprite": {
            "red": sprites.red_ship_3,
            "blue": sprites.blue_ship_3,
            "green": sprites.green_ship_3
        }
    },
    "fast": {
        "lives": 3,
        "shoot_distance": 269.21,
        "velocity": 450,
        "description": "Nave mais veloz",
        "sprite": {
            "red": sprites.red_ship_1,
            "blue": sprites.blue_ship_1,
            "green": sprites.green_ship_1
        }
    },
    "furious": {
        "lives": 3,
        "shoot_distance": 210,
        "velocity": 350,
        "description": "Nave mais furiosa, com o tiro 14,19% mais rápido",
        "sprite": {
            "red": sprites.red_ship_2,
            "blue": sprites.blue_ship_2,
            "green": sprites.green_ship_2
        }
    }
}

colors = ["red", "green", "blue"]
ships = ["resistant", "fast", "furious"]


class ChooseShipScene(Scene):
    def __init__(self, screen):
        self.screen = screen
        self.background = Background(self.screen)

        self.game_config_name = "resistant"
        self.ship_color = "red"

    def draw(self):
        self.background.draw()
        s = pygame.Surface((1000, 600), pygame.SRCALPHA)
        s.fill((0, 0, 0, 150))  # valor de alpha sobre a cor
        self.screen.blit(s, (0, 0))

        width, height = self.screen.get_size()

        description = game_configs[self.game_config_name]["description"]
        text = font.render(description, True, (200, 200, 200))
        pos = text.get_rect(center=(width / 2, 200))
        self.screen.blit(text, pos)

        sprite = pygame.transform.scale(game_configs[self.game_config_name]["sprite"][self.ship_color],
                                        (int(SHIP_SIZE.x), int(SHIP_SIZE.y)))
        self.screen.blit(sprite, (width / 2 - SHIP_SIZE.x / 2, height / 2 - SHIP_SIZE.y / 2))

    def update(self, dt, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    index = (colors.index(self.ship_color) + 1) % 3
                    self.ship_color = colors[index]
                elif event.key == pygame.K_LEFT:
                    index = (colors.index(self.ship_color) - 1) % 3
                    self.ship_color = colors[index]
                elif event.key == pygame.K_UP:
                    index = (ships.index(self.game_config_name) + 1) % 3
                    self.game_config_name = ships[index]
                elif event.key == pygame.K_DOWN:
                    index = (ships.index(self.game_config_name) - 1) % 3
                    self.game_config_name = ships[index]
                elif event.key == pygame.K_RETURN:
                    self.emit("START_GAME", game_config=game_configs[self.game_config_name], ship_color=self.ship_color)

        self.background.update(dt)
