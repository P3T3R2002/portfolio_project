from circleshape import *
from Planet.shoot import *
from constants import ENEMY_CONSTANTS

class Enemy(Character):
    def __init__(self, x, y, r, diff, score = 0):
        super().__init__(x, y, score, r)
        self.shoot_timer = 0
        self.difficulty = diff
    
    def draw(self, screen):
        pygame.draw.polygon(screen, 'RED', self.triangle(), width=2)

    def triangle(self):
        forward = pygame.Vector2(-1, 0)
        right = pygame.Vector2(0, -1) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]    

    def update(self, dt):
        self.move(dt)
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
        else:
            self.shoot_timer = 0
        self.planet_shoot()
        
    def move(self, dt):
        self.position += self.velocity * dt
    
    def planet_shoot(self):
        if self.shoot_timer == 0:
            bullet = Planet_Shoot(self.position.x-self.radius-ENEMY_CONSTANTS["weapon"]["projectile"]["radius"], self.position.y, ENEMY_CONSTANTS["weapon"]["projectile"]["radius"], False)
            bullet.velocity = pygame.Vector2(-1, 0)*ENEMY_CONSTANTS["weapon"]["projectile"]["speed"][self.difficulty-1]
            self.shoot_timer = ENEMY_CONSTANTS["weapon"]["rate_of_fire"][self.difficulty-1]

    def collsion(self, other):
        if other.friendly:
            return super().collsion(other)
        return False
