import pygame
from objects.enemy import Enemy

from src.objects.background import Background
from src.objects.ship import Ship
from src.objects.shot import Shot, SHOT_SIZE
import random


class GameScene:
    def __init__(self, screen):
        self.screen = screen
        self.background = Background(self.screen)
        self.ship = Ship(screen, 300)
        self.shots = []
        self.enemies=[]

    def limit_ship_position(self):
        if self.ship.pos.y < 0:
            self.ship.pos.y = 0
        elif self.ship.pos.y + self.ship.size.y > self.screen.get_height():
            self.ship.pos.y = self.screen.get_height() - self.ship.size.y

    def shoot(self):
        pos = self.ship.pos + self.ship.size / 2 - SHOT_SIZE / 2
        shot = Shot(self.screen, initial_pos=pos, speed=400)

        is_able_to_shoot = len(self.shots) == 0 or self.shots[-1].pos.x - self.ship.pos.x > 150
        if is_able_to_shoot:
            self.shots.append(shot)

    def remove_distant_shots(self):
        for shot in self.shots:
            if shot.pos.x > self.screen.get_width():
                self.shots.remove(shot)

    def enemy(self):
        enemy=Enemy(self.screen,speed=200 ,typo=random.randint(1,5))   
        enemy.spawn()
        is_able_to_spawn= len(self.enemies)<=4 or 1000-self.enemies[-1].pos.x > 40
        if is_able_to_spawn:
            self.enemies.append(enemy)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.ship.move_up(dt)
        if keys[pygame.K_DOWN]:
            self.ship.move_down(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_x]:
            self.enemy()



        self.background.update(dt)
        self.limit_ship_position()

        for shot in self.shots:
            shot.update(dt)

        for enemy in self.enemies:
            enemy.update(dt)    

        self.remove_distant_shots()
    
    
    def draw(self):
        self.background.draw()

        for shot in self.shots:
            shot.draw()
        for enemy in self.enemies:
            enemy.draw() 
        self.ship.draw()

        
        