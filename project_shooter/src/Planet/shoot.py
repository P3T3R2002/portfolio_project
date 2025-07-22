from circleshape import *
from constants import PLAYER_CONSTANTS, ENEMY_CONSTANTS

class Planet_Shoot(CircleShape):
    def __init__(self, x, y, f, rotation):
        if f:
            super().__init__(x, y, PLAYER_CONSTANTS["weapon"]["projectile"]["radius"], PLAYER_CONSTANTS['weapon']['projectile']['source'])
        else:
            super().__init__(x, y, ENEMY_CONSTANTS["weapon"]["projectile"]["radius"], ENEMY_CONSTANTS['weapon']['projectile']['source'])

        self.image = pygame.transform.rotate(self.image, -rotation+180)
        self.image_rect = self.image.get_rect(center=self.position)
        self.friendly = f
    
    def draw(self, screen):
        screen.blit(self.image, self.image_rect)
        
    def update(self, dt):
        self.position += self.velocity*dt
        self.image_rect.center = self.position

    def collsion(self, other):
        if self.friendly != other.friendly:
            return super().collsion(other)
        return False
    
    