from circleshape import *
from constants import PLAYER_CONSTANTS

class Space_Shoot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_CONSTANTS["weapon"]["projectile"]["radius"])
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width=2)
        
    def update(self, dt, camera):
        self.position += self.velocity*dt - camera.velocity
