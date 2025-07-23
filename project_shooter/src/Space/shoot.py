from circleshape import *
from constants import PLAYER_CONSTANTS, MAP_HIGHT, MAP_WIDTH

class Space_Shoot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, PLAYER_CONSTANTS["weapon"]["projectile"]["radius"], PLAYER_CONSTANTS['weapon']['projectile']['source'])
        self.image = pygame.transform.rotate(self.image, -rotation+180)
        self.image_rect = self.image.get_rect(center=self.position)
            
    def update(self, dt, camera):
        self.position += self.velocity*dt - camera.velocity
        self.image_rect.center = self.position
    
    def inside(self):
        return (-MAP_WIDTH/2 <= self.position.x <= MAP_WIDTH/2 and
            -MAP_HIGHT/2 <= self.position.y <= MAP_HIGHT/2)

