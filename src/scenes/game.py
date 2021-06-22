from random import randint

import pygame

from src.objects.background import Background
from src.objects.enemy import Enemy
from src.objects.ship import Ship
from src.objects.shot import Shot, SHOT_SIZE
from src.scenes.scene import Scene


class GameScene(Scene):
    def __init__(self, screen):
        self.screen = screen
        self.background = Background(self.screen)
        self.ship = Ship(screen, 350)
        self.shots = []
        self.enemies = []

    def limit_ship_position(self):
        if self.ship.pos.y < 0:
            self.ship.pos.y = 0
        elif self.ship.pos.y + self.ship.size.y > self.screen.get_height():
            self.ship.pos.y = self.screen.get_height() - self.ship.size.y

    def shoot(self):
        pos = self.ship.pos + self.ship.size / 2 - SHOT_SIZE / 2
        shot = Shot(self.screen, initial_pos=pos, speed=600)

        is_able_to_shoot = len(self.shots) == 0 or self.shots[-1].pos.x - self.ship.pos.x > 250
        if is_able_to_shoot:
            self.shots.append(shot)

    def spawn_enemy(self):
        enemy = Enemy(self.screen, speed=randint(250, 350), what_enemy=randint(1,4))

        is_able_to_spawn = len(self.enemies) == 0 or self.screen.get_width() * 1.5 - self.enemies[-1].pos.x > 250
        if is_able_to_spawn:
            self.enemies.append(enemy)

    def remove_intercepted_enemies(self):
        for enemy in self.enemies:
            for shot in self.shots:
                if shot.collides_with(enemy):
                    self.enemies.remove(enemy)
                    self.shots.remove(shot)
                    break

    def remove_distant_shots(self):
        for shot in self.shots:
            if shot.pos.x > self.screen.get_width():
                self.shots.remove(shot)

    def update(self, dt):
        keys = pygame.key.get_pressed()

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
                self.emit("GAME_OVER")

    def draw(self):
        self.background.draw()

        for shot in self.shots:
            shot.draw()

        for enemy in self.enemies:
            enemy.draw()

        self.ship.draw()
