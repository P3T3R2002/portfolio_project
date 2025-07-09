# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from camera import *
from constants import*
from Planet.player import*

def Planet(planet):
    dt = 0
    screen = pygame.display.get_surface()
    game_time = pygame.time.Clock()

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

        pygame.display.flip()
        dt = game_time.tick(60)/1000


