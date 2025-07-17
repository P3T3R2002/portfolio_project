import pygame
from constants import MAP_WIDTH, MAP_HIGHT


class Camera:
    def __init__(self):
        self.position = pygame.Vector2(0, 0)
        self.velocity = pygame.Vector2(0, 0)
    
    def move(self, forward, dt):
        self.velocity = forward * dt
        self.position -= self.velocity 
    
    def draw(self, screen):
        pygame.draw.rect(screen, "yellow", pygame.Rect(((MAP_WIDTH/2-self.position.x)/100, (MAP_HIGHT-self.position.y)/100), (10, 10)), 2)
    
    def reset_velocity(self):
        self.velocity = pygame.Vector2(0, 0)

    def is_visible(self, screen, obj):
        return (-obj.radius <= obj.position.x <= screen.get_width() + obj.radius and
            -obj.radius <= obj.position.y <= screen.get_height() + obj.radius)
    
    def set_pos(self, x, y):
        self.position = pygame.Vector2(x, y)

    def __repr__(self) -> str:
        return f"{self.position[0]}:{self.position[1]}"