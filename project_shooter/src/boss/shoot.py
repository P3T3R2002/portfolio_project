from circleshape import *
from constants import PLAYER_CONSTANTS, SCREEN_HEIGHT, SCREEN_WIDTH

class Boss_Shoot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, PLAYER_CONSTANTS["weapon"]["projectile"]["radius"], PLAYER_CONSTANTS['weapon']['projectile']['source'])
        self.image = pygame.transform.rotate(self.image, -rotation+180)
        self.image_rect = self.image.get_rect(center=self.position)
        self.friendly = True
            
    def update(self, dt):
        self.position += self.velocity*dt
        self.image_rect.center = self.position
    
    def inside(self):
        return (-self.radius <= self.position.x <= SCREEN_WIDTH+self.radius and
            -self.radius <= self.position.y <= SCREEN_HEIGHT+self.radius)

    def collsion(self, other):
        if self.friendly != other.friendly:
            return super().collsion(other)
        return False
    