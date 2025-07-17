from circleshape import *
from constants import PLAYER_CONSTANTS, MAP_HIGHT, MAP_WIDTH

class Space_Shoot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_CONSTANTS["weapon"]["projectile"]["radius"])
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width=2)
        
    def update(self, dt, camera):
        self.position += self.velocity*dt - camera.velocity
    
    def inside(self):
        return (-MAP_WIDTH/2 <= self.position.x <= MAP_WIDTH/2 and
            -MAP_HIGHT/2 <= self.position.y <= MAP_HIGHT/2)

