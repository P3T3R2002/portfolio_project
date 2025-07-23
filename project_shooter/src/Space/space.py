import pygame
from player import *
from camera import *
from Space.shoot import *
from Space.asteroid import *
from Space.game_map import *
from Space.asteroidfield import *

def Space(planets, player, camera, hud):
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

        winner = False
        score = 0
        hud.update(player)
        while not winner:
            screen.fill('black')
            for thing in updatable:
                thing.update(dt, camera)
            player.update(dt, camera)
            if planets.update(dt, camera):
                print(f"You won!\nYour score: {player.score}")
                return False

            planets.draw(screen)
            for thing in drawable:
                if camera.is_visible(thing):
                    thing.draw(screen)
            player.draw(screen)
            hud.draw(screen)
            camera.draw(screen)

            for asteroid in asteroids:
                for bullet in shoots:
                    if bullet.collsion(asteroid): 
                        score += 1  
                        player.score += 1  
                        hud.update_score(player.score)               
                        asteroid.split()
                        bullet.kill()
                if asteroid.collsion(player):
                    print(f"Game Over!\nYour score: {player.score}")
                    player.dead = True
                    return True
                
            for bullet in shoots:
                if not bullet.inside():
                    bullet.kill()

            planet = planets.collsion(player)
            if planet:
                return planet

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
  
            pygame.display.flip()
            dt = game_time.tick(120)/1000


