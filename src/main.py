import sys

import pygame

sys.path.append('.')

from src.scenes.game import GameScene
from src.scenes.gameover import GameOver

from src.sprites import sprites

# Inicia os módulos do pygame
pygame.init()

# Coloca o título e o icon 
icon = sprites.icon
pygame.display.set_caption("Jornada do rorô")
pygame.display.set_icon(icon)

# Cria a tela do jogo, com o tamanho de 1000x600
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()

# Cria a cena do jogo
game_scene = GameScene(screen)
game_over_scene = GameOver(screen)

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