# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import*
from player import*

def Planet(planet, player):
    dt = 0
    screen = pygame.display.get_surface()
    game_time = pygame.time.Clock()
    planet.completed()

    while True:
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        enemys = pygame.sprite.Group()
        shoots = pygame.sprite.Group()

        Planet_Shoot.containers = (shoots, updatable, drawable)
        Enemy.containers = (enemys, updatable, drawable)
        Planet_Player.containers = (updatable, drawable)
        

        dead = False
        winner = False
        while not dead and not winner:
            screen.fill('black')
            for thing in updatable:
                thing.update(dt)
            player.update(dt)
            planet.update(dt)

            for thing in drawable:
                thing.draw(screen)
            player.draw(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None

            pygame.display.flip()
            dt = game_time.tick(60)/1000


 