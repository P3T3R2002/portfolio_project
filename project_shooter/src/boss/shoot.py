from circleshape import *
from constants import PLAYER_CONSTANTS, ENEMY_CONSTANTS, SCREEN_HEIGHT, SCREEN_WIDTH

class Boss_Bullet(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, PLAYER_CONSTANTS["weapon"]["projectile"]["radius"], PLAYER_CONSTANTS['weapon']['projectile']['source'])
        self.image = pygame.transform.rotate(self.image, -rotation+180)
        self.image_rect = self.image.get_rect(center=self.position)
        self.friendly = True
            
    def update(self, dt):
        super().update(dt)
        if not self.inside():
            self.kill()
    
    def inside(self):
        return (-self.radius <= self.position.x <= SCREEN_WIDTH+self.radius and
            -self.radius <= self.position.y <= SCREEN_HEIGHT+self.radius)

    def collsion(self, other):
        if self.friendly != other.friendly:
            return super().collsion(other)
        return False
    

class Boss_Rocket(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, ENEMY_CONSTANTS["weapon"]["projectile"]["radius"], ENEMY_CONSTANTS['weapon']['projectile']['source'])
        self.image = pygame.transform.rotate(self.image, -rotation+180)
        self.image_rect = self.image.get_rect(center=self.position)
        self.friendly = False
            
    def update(self, dt):
        super().update(dt)
        if not self.inside():
            self.kill()
    
    def inside(self):
        return (-self.radius <= self.position.x <= SCREEN_WIDTH+self.radius and
            -self.radius <= self.position.y <= SCREEN_HEIGHT+self.radius)

    def collsion(self, other):
        if self.friendly != other.friendly:
            return super().collsion(other)
        return False