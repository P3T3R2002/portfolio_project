# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from camera import *
from constants import*
from Space.player import*
from Space.asteroid import*
from Space.game_map import *
from Space.asteroidfield import*

def Space(planets):
    dt = 0
    screen = pygame.display.get_surface()
    game_time = pygame.time.Clock()

    while True:
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        shoots = pygame.sprite.Group()

        Shoot.containers = (shoots, updatable, drawable)

        Asteroid.containers = (asteroids, updatable, drawable)

        AsteroidField.containers = (updatable)
        asteroidfield = AsteroidField()

        Space_Player.containers = (updatable, drawable)
        player = Space_Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


        camera = Camera()
        dead = False
        winner = False
        while not dead and not winner:
            screen.fill('black')
            for thing in updatable:
                thing.update(dt, camera)
            winner = planets.update(dt, camera)

            planets.draw(screen)
            for thing in drawable:
                if camera.is_visible(screen, thing):
                    thing.draw(screen)
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

            planet = planets.collsion(player)
            if planet:
                return planet

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None

            pygame.display.flip()
            dt = game_time.tick(60)/1000


