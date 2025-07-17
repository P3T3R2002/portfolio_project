import pygame
import random
from enemy import *
from circleshape import *
from constants import ENEMY_CONSTANTS, SCREEN_HEIGHT

class Planet:
    def __init__(self, dif=1):
        self.__completed = False
        self.difficulty = dif
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity, diff):
        enemy = Enemy(position.x, position.y, radius, diff)
        enemy.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > ENEMY_CONSTANTS["ship"]["spawn_rate"][self.difficulty-1]:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            speed = ENEMY_CONSTANTS["ship"]["speed"][self.difficulty-1]
            velocity = pygame.Vector2(-random.randint(speed[1], speed[0]), 0)
            position = pygame.Vector2(ENEMY_CONSTANTS["ship"]["spawn_line"], SCREEN_HEIGHT * random.randint(10, 90)/100)
            self.spawn(ENEMY_CONSTANTS["ship"]["radius"], position, velocity, self.difficulty)

    def completed(self):
        self.__completed = True

    def get_completion(self):
        return self.__completed

    def get_difficulty(self):
        return self.difficulty
