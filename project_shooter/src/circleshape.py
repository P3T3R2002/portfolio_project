import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collsion(self, other):
        distance = self.position.distance_to(other.position)
        return distance < self.radius + other.radius
    

class Character(CircleShape):
    def __init__(self, x, y, score, r):
        super().__init__(x, y, r)
        self.rotation = 270
        self.shoot_timer = 0
        self.score = score
