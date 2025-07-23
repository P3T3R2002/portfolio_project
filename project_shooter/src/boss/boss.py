from boss.asteroidfield import *
from boss.shoot import *

class Boss:
    def __init__(self):
        self.HP = 1000
        self.pre_faze = 1000
        self.asteroid_field = None


    def start_boss(self, player, hud):
        dt = 0
        screen = pygame.display.get_surface()
        game_time = pygame.time.Clock()

        while True:
            updatable = pygame.sprite.Group()
            drawable = pygame.sprite.Group()
            asteroids = pygame.sprite.Group()
            shoots = pygame.sprite.Group()

            Boss_Shoot.containers = (shoots, updatable, drawable)

            Asteroid.containers = (asteroids, updatable, drawable)

            AsteroidField.containers = (updatable)
            self.asteroidfield = AsteroidField()

            hud.update_stats(player)
            while True:
                screen.fill('black')
                for thing in updatable:
                    thing.update(dt)
                player.update(dt)

                for thing in drawable:
                    thing.draw(screen)
                player.draw(screen)
                hud.draw(screen)

                for asteroid in asteroids:
                    for bullet in shoots:
                        if asteroid.collsion(bullet): 
                            self.pre_faze -= 1  
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
                for asteroid in asteroids:
                    if not asteroid.inside():
                        asteroid.kill()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return None
    
                pygame.display.flip()
                dt = game_time.tick(120)/1000

            