# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import*
from player import*
from asteroid import*
from asteroidfield import*
from camera import *

def main():
    pygame.init()
    game_time = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shoots = pygame.sprite.Group()

    Shoot.containers = (shoots, updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    camera = Camera(player)

    while True:
        screen.fill('black')
        for thing in updatable:
            thing.update(dt, camera)

        for thing in drawable:
            thing.draw(screen)

        for asteroid in asteroids:
            if not asteroid.collsion(player):
                print(f"Game Over!\nYour score: {player.score}")
                return

        for asteroid in asteroids:
            for bullet in shoots:
                if not asteroid.collsion(bullet): 
                    player.score += 1                   
                    asteroid.split()
                    bullet.kill()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()
        dt = game_time.tick(60)/1000



if __name__ == "__main__":
    main()
