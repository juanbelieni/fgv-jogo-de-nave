import sys

import pygame

pygame.init()

sys.path.append('.')

from src.scenes.main_menu import CreditsScene
from src.scenes.main_menu import InstructionsScene
from src.scenes.game import GameScene
from src.scenes.gameover import GameOverScene
from src.sprites import sprites
from src.scenes.choose_ship import ChooseShipScene
from src.scenes.main_menu import MenuScene
# from src.sound_fx import sound_fx

# Coloca o título e o icon
icon = sprites.icon
pygame.display.set_caption("Jornada do rorô")
pygame.display.set_icon(icon)

# Cria a tela do jogo, com o tamanho de 1000x600
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()

# Cria a cena do jogo
# scene = GameScene(screen)
#scene = ChooseShipScene(screen)
scene = MenuScene(screen)

# Controle se o jogo está sendo executado ou não
running = True


# Inicia musica previamente carregada em loop infinito
pygame.mixer.music.play(loops = -1, start = 0.7)


def handle_scene_event(ev, **args):
    global scene

    if ev == "RESTART":
        scene = MenuScene(screen)
    if ev == "INSTRUCTIONS":
            scene = InstructionsScene(screen)
    if ev == "CREDITS":
        scene = CreditsScene(screen)
    elif ev == "CHOOSE_SHIP":
        scene = ChooseShipScene(screen)
    elif ev == "GAME_OVER":
        scene = GameOverScene(screen)
    elif ev == "START_GAME":
        scene = GameScene(screen, **args)


while running:
    pygame.display.update()

    events = pygame.event.get()

    for event in events:
        is_quitting = event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE)
        if is_quitting:
            running = False

    dt = clock.tick() / 1000

    # Realiza os cálculos da parte lógica do jogo
    scene.update(dt, events)

    # Desenha na tela
    scene.draw()

    scene.on_event(handle_scene_event)
