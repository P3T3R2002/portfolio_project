import pygame
import random
from constants import ENEMY_CONSTANTS, SCREEN_HEIGHT
from circleshape import *
from player import Enemy

class Planet:
    def __init__(self, dif=1):
        self.__completed = False
        self.__difficulty = dif
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity, diff):
        enemy = Enemy(position.x, position.y, radius, diff)
        enemy.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > ENEMY_CONSTANTS["ship"]["spawn_rate"][self.__difficulty]:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            speed = ENEMY_CONSTANTS["ship"]["speed"][self.__difficulty-1]
            velocity = pygame.Vector2(-random.randint(speed[1], speed[0]), 0)
            position = pygame.Vector2(ENEMY_CONSTANTS["ship"]["spawn_line"], SCREEN_HEIGHT * random.randint(10, 90)/100)
            self.spawn(ENEMY_CONSTANTS["ship"]["radius"], position, velocity, self.__difficulty)

    def completed(self):
        self.__completed = True

    def get_completion(self):
        return self.__completed

    def get_difficulty(self):
        return self.__difficulty
