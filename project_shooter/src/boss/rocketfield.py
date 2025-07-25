import random
from boss.shoot import *
from circleshape import *
from constants import ENEMY_CONSTANTS

class Rocket_Field(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.__shoot_timer = 0
        self.difficulty = 4
        self.friendly = False
    
    def update(self, dt):
        if self.__shoot_timer > 0:
            self.__shoot_timer -= dt
        else:
            self.__shoot_timer = 0
            self.shoot_rocket()
    
    def shoot_rocket(self):
        if self.__shoot_timer == 0:
            position = pygame.Vector2(ENEMY_CONSTANTS["ship"]["spawn_line"], SCREEN_HEIGHT * random.randint(10, 90)/100)
            bullet = Boss_Rocket(position.x, position.y, 90)
            bullet.velocity = pygame.Vector2(-1, 0)*ENEMY_CONSTANTS["weapon"]["projectile"]["speed"][self.difficulty-1]
            self.__shoot_timer = 0.2

    def collsion(self, other):
        if other.friendly:
            return super().collsion(other)
        return False
