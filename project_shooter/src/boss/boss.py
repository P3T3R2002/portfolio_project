from boss.shoot import *
from circleshape import *
from boss.rocketfield import *
from boss.asteroidfield import *
from constants import BOSS_CONSTANTS, SCREEN_HEIGHT


class Boss(Character):
    def __init__(self):
        super().__init__(-100, -100, 0, BOSS_CONSTANTS['radius'], BOSS_CONSTANTS['source'])
        self.image = pygame.transform.rotate(self.image, 180)
        self.image_rect = self.image.get_rect(center=self.position)
        self.friendly = False
        self.HP = 200
        self.pre_faze = 500
        self.score = 0
        self.phase1 = True
        self.asteroid_field = None
        self.rocket_field = None


    def start_boss(self, player, hud):
        dt = 0
        screen = pygame.display.get_surface()
        game_time = pygame.time.Clock()

        while True:
            updatable = pygame.sprite.Group()
            drawable = pygame.sprite.Group()
            asteroids = pygame.sprite.Group()
            bullets = pygame.sprite.Group()
            rockets = pygame.sprite.Group()

            Boss_Rocket.containers = (rockets, updatable, drawable)
            Boss_Bullet.containers = (bullets, updatable, drawable)

            Asteroid.containers = (asteroids, updatable, drawable)

            Rocket_Field.containers = (updatable)
            AsteroidField.containers = (updatable)
            self.asteroidfield = AsteroidField()

            while True:
                if self.pre_faze < 0 and self.phase1:
                    self.position  = (1200, SCREEN_HEIGHT/2)
                    self.image_rect.center = self.position
                    self.phase1 = False
                    hud.fight.set_max_score(200)
                    self.score = 0
                    self.rocket_field = Rocket_Field()
                    print("rockets")
                screen.fill('black')
                for thing in updatable:
                    thing.update(dt)
                player.update(dt)

                for thing in drawable:
                    thing.draw(screen)
                player.draw(screen)
                self.draw(screen)
                hud.draw(screen)

                for asteroid in asteroids:
                    for bullet in bullets:
                        if asteroid.collsion(bullet): 
                            if self.phase1:
                                self.pre_faze -= 1  
                                hud.update_fight(self.score) 
                            self.score += 1    
                            player.score += 1            
                            asteroid.split()
                            bullet.kill()
                    if asteroid.collsion(player):
                        print(f"Game Over!\nYour score: {player.score}")
                        player.dead = True
                        return True
                    
                for rocket in rockets:
                    for bullet in bullets:
                        if bullet.collsion(rocket):
                            bullet.kill()
                            rocket.kill()
                            player.score += 1
                            self.score += 1
                    if rocket.collsion(player):
                        print(f"Game Over!\nYour score: {player.score}")
                        player.dead = True
                        return True

                for bullet in bullets:
                    if bullet.collsion(self):
                        self.HP -= 1
                        hud.update_fight(-self.HP+200)  
                        bullet.kill()
                        print("HP", self.HP)
                        if self.HP <= 0:
                            player.winner = True
                            return True
                    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return None
    
                pygame.display.flip()
                dt = game_time.tick(120)/1000

            