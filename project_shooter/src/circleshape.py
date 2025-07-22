import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, image_url = None):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.image = image_url
        self.image_rect = None
        if image_url:
            self.image = image_url
            self.image_rect = self.image.get_rect(center=self.position)

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
    def __init__(self, x, y, score, r, url):
        super().__init__(x, y, r, url)
        self.rotation = 180
        self.score = score
