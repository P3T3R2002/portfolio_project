from circleshape import *

class Planet_Shoot(CircleShape):
    def __init__(self, x, y, r, f):
        super().__init__(x, y, r)
        self.friendly = f
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width=2)
        
    def update(self, dt):
        self.position += self.velocity*dt

    def collsion(self, other):
        if self.friendly != other.friendly:
            return super().collsion(other)
        return False
    
    