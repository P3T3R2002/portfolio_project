import random
from circleshape import*
from constants import ASTEROID_CONSTANTS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, image_url = None):
        super().__init__(x, y, radius, image_url)
    
    def draw(self, screen):
        screen.blit(self.image, self.image_rect)
        
    def update(self, dt, camera):
        self.position += self.velocity*dt - camera.velocity
        self.image_rect.center = self.position

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_CONSTANTS['min_radius']:
            return
        angle = random.uniform(20, 50)
        vel1 = self.velocity.rotate(angle)
        vel2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_CONSTANTS['min_radius']
        url = None
        if new_radius == ASTEROID_CONSTANTS['min_radius']:
            url = ASTEROID_CONSTANTS['kinds']["SMALL"]
        else:
            url = ASTEROID_CONSTANTS['kinds']["MIDDLE"]
        aster1 = Asteroid(self.position[0], self.position[1], new_radius, url)
        aster1.velocity = vel1*1.2
        aster2 = Asteroid(self.position[0], self.position[1], new_radius, url)
        aster2.velocity = vel2*1.2

    def __repr__(self) -> str:
        return f"{self.position[0]}:{self.position[1]}, radious: {self.radius}"
