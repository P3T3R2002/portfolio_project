import pygame
import random
from constants import *
from circleshape import *
from player import Enemy

class Planet:
    def __init__(self, dif=1):
        self.__completed = False
        self.__difficulty = dif
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        enemy = Enemy(position.x, position.y, radius)
        enemy.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > ENEMY_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            velocity = pygame.Vector2(-random.randint(30, 50), 0)
            position = pygame.Vector2(ENEMY_X_LINE, SCREEN_HEIGHT * random.randint(10, 90)/100)
            self.spawn(ENEMY_RADIUS, position, velocity)

    def completed(self):
        self.__completed = True

    def get_completion(self):
        return self.__completed

    def get_difficulty(self):
        return self.__difficulty
