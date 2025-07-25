from circleshape import *
from Planet.shoot import *
from constants import ENEMY_CONSTANTS

class Enemy(Character):
    def __init__(self, x, y, r, diff, score = 0):
        super().__init__(x, y, score, r, ENEMY_CONSTANTS["ship"]["source"])
        self.__shoot_timer = 0
        self.difficulty = diff
        self.friendly = False
        self.image = pygame.transform.rotate(self.image, 180)
    
    def update(self, dt):
        self.move(dt)
        if self.__shoot_timer > 0:
            self.__shoot_timer -= dt
        else:
            self.__shoot_timer = 0
        self.planet_shoot()
        
    def move(self, dt):
        self.position += self.velocity * dt
        self.image_rect.center = self.position
    
    def planet_shoot(self):
        if self.__shoot_timer == 0:
            bullet = Planet_Shoot(self.position.x-self.radius-ENEMY_CONSTANTS["weapon"]["projectile"]["radius"], self.position.y, False, 90)
            bullet.velocity = pygame.Vector2(-1, 0)*ENEMY_CONSTANTS["weapon"]["projectile"]["speed"][self.difficulty-1]
            self.__shoot_timer = ENEMY_CONSTANTS["weapon"]["rate_of_fire"][self.difficulty-1]

    def collsion(self, other):
        if other.friendly:
            return super().collsion(other)
        return False
