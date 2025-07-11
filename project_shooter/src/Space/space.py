# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import*
from Space.camera import *
from player import *
from Space.asteroid import *
from Space.game_map import *
from Space.asteroidfield import *

def Space(planets, player, camera):
    dt = 0
    screen = pygame.display.get_surface()
    game_time = pygame.time.Clock()

    while True:
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        shoots = pygame.sprite.Group()

        Space_Shoot.containers = (shoots, updatable, drawable)

        Asteroid.containers = (asteroids, updatable, drawable)

        AsteroidField.containers = (updatable)
        asteroidfield = AsteroidField()

        dead = False
        winner = False
        while not dead and not winner:
            screen.fill('black')
            for thing in updatable:
                thing.update(dt, camera)
            player.update(dt, camera)
            if planets.update(dt, camera):
                return None

            planets.draw(screen)
            for thing in drawable:
                if camera.is_visible(screen, thing):
                    thing.draw(screen)
            player.draw(screen)
            planets.draw_minimap(screen)
            camera.draw(screen)

            for asteroid in asteroids:
                for bullet in shoots:
                    if asteroid.collsion(bullet): 
                        player.score += 1                   
                        asteroid.split()
                        bullet.kill()
                if asteroid.collsion(player):
                    print(f"Game Over!\nYour score: {player.score}")
                    dead = True
                    planets.reset_pos()
                    camera.set_pos(0, 0)

            planet = planets.collsion(player)
            if planet:
                return planet

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None

            pygame.display.flip()
            dt = game_time.tick(60)/1000


