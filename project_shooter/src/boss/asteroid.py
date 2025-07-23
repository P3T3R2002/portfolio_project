import random
from circleshape import*
from constants import ASTEROID_CONSTANTS, SCREEN_HEIGHT, SCREEN_WIDTH


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, image_url = None):
        super().__init__(x, y, radius, image_url)
        
    def update(self, dt):
        self.position += self.velocity*dt
        self.image_rect.center = self.position
    
    def inside(self):
        return (-100 <= self.position.x <= SCREEN_WIDTH+100 and
            -100 <= self.position.y <= SCREEN_HEIGHT+100)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_CONSTANTS['min_radius']:
            return
        angle = random.uniform(-25, 25)
        for i in range(-2, 2):
            vel = self.velocity.rotate(angle+i*25)
            new_radius = self.radius - ASTEROID_CONSTANTS['min_radius']
            url = None
            if new_radius == ASTEROID_CONSTANTS['min_radius']:
                url = ASTEROID_CONSTANTS['kinds']["SMALL"]
            else:
                url = ASTEROID_CONSTANTS['kinds']["MIDDLE"]
            aster = Asteroid(self.position[0], self.position[1], new_radius, url)
            aster.velocity = vel*1.2  


    def __repr__(self) -> str:
        return f"{self.position[0]}:{self.position[1]}, radious: {self.radius}"