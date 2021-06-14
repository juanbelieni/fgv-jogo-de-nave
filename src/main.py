import sys

import pygame

sys.path.append('.')

from scenes.game import GameScene

# Inicia os módulos do pygame
pygame.init()

# Cria a tela do jogo, com o tamanho de 1000x600
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()

# Cria a cena do jogo
game_scene = GameScene(screen)

# Controle se o jogo está sendo executado ou não
running = True

while running:
    pygame.display.update()

    events = pygame.event.get()
    for event in events:
        is_quitting = event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE)
        if is_quitting:
            running = False

    dt = clock.tick() / 1000

    # Realiza os cálculos da parte lógica do jogo
    game_scene.update(dt)

    # Desenha na tela
    game_scene.draw()
