import sys
from typing import ChainMap

sys.path.append('.')

import pygame
pygame.init()

from src.scenes.game import GameScene


# Cria a tela do jogo, com o tamanho de 1200x800
screen = pygame.display.set_mode((1000, 600))

# Cria a cena do jogo
game_scene = GameScene(screen)

# Controle se o jogo está sendo executado ou não
running = True



while running:
    pygame.display.update()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

        
    # Realiza os cálculos da parte lógica do jogo
    game_scene.step(events)

    # Desenha na tela
    game_scene.draw()



