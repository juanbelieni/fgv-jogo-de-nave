from random import randint

import pygame
from pygame.constants import K_p

from src.objects.background import Background
from src.objects.enemy import Enemy
from src.objects.ship import Ship
from src.objects.S2 import S2
from src.objects.shot import Shot, SHOT_SIZE
from src.scenes.scene import Scene



class GameScene(Scene):
    def __init__(self, screen, game_config, ship_color):
        self.screen = screen
        self.background = Background(self.screen)
        self.game_config = game_config
        self.ship = Ship(screen, game_config["sprite"][ship_color], self.game_config["velocity"])
        
        self.font_name = 'src/Fonte_do_game.TTF'
        self.pause = False
        
        self.shots = []
        self.enemies = []
        self.score = 0

        self.S2 = []
        lives = self.game_config["lives"]
        for counter in range(lives + 1):
            self.S2.append(S2(self.screen))

    def limit_ship_position(self):
        if self.ship.pos.y < 0:
            self.ship.pos.y = 0
        elif self.ship.pos.y + self.ship.size.y > self.screen.get_height():
            self.ship.pos.y = self.screen.get_height() - self.ship.size.y

    def shoot(self):
        pos = self.ship.pos + self.ship.size / 2 - SHOT_SIZE / 2
        shot = Shot(self.screen, initial_pos=pos, speed=600)

        is_able_to_shoot = len(self.shots) == 0 or self.shots[-1].pos.x - self.ship.pos.x > self.game_config[
            "shoot_distance"]
        if is_able_to_shoot:
            self.shots.append(shot)

    def spawn_enemy(self):
        enemy = Enemy(self.screen, speed=randint(250, 350), what_enemy=randint(1, 4))

        is_able_to_spawn = len(self.enemies) == 0 or self.screen.get_width() * 1.5 - self.enemies[-1].pos.x > 250
        if is_able_to_spawn:
            self.enemies.append(enemy)

    def remove_intercepted_enemies(self):
        for enemy in self.enemies:
            for shot in self.shots:
                if shot.collides_with(enemy):
                    self.score += 1
                    self.enemies.remove(enemy)
                    self.shots.remove(shot)
                    break

    def remove_distant_shots(self):
        for shot in self.shots:
            if shot.pos.x > self.screen.get_width():
                self.shots.remove(shot)

    def update(self, dt, events):
        keys = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == K_p:
                self.pause = not self.pause
        if self.pause:
            return None

        if keys[pygame.K_UP]:
            self.ship.move_up(dt)
        if keys[pygame.K_DOWN]:
            self.ship.move_down(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.background.update(dt)
        self.limit_ship_position()
        self.spawn_enemy()

        for shot in self.shots:
            shot.update(dt)

        for enemy in self.enemies:
            enemy.update(dt)

        self.remove_distant_shots()
        self.remove_intercepted_enemies()

        for enemy in self.enemies:
            if enemy.pos.x < 0:
                self.S2.pop(-1)
                self.enemies.remove(enemy)

        if len(self.S2) <= 1:
            self.emit("GAME_OVER")

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.screen.blit(text_surface,text_rect)


    def draw(self):
        self.background.draw()

        for shot in self.shots:
            shot.draw()

        for enemy in self.enemies:
            enemy.draw()
        for counter in range(1, len(self.S2)):
            self.S2[counter].draw(counter)

        self.ship.draw()


        self.draw_text(f"SCORE {self.score}", 40, 800, 20)

        if self.pause:
            s = pygame.Surface((1000, 600), pygame.SRCALPHA)
            s.fill((0, 0, 0, 150))  # valor de alpha sobre a cor
            self.screen.blit(s, (0, 0))


            text = "JOGO PAUSADO * APERTE P PARA DESPAUSAR"
            font = pygame.font.Font('src/Fonte_do_game.TTF', 20)
            text_surface = font.render(text, True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.center = (self.screen.get_width()/2,self.screen.get_height()/2)
            self.screen.blit(text_surface,text_rect)

