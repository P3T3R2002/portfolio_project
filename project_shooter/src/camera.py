import pygame
from constants import*


class Camera:
    def __init__(self, player):
        self.position = pygame.Vector2(0, 0)
        self.velocity = pygame.Vector2(0, 0)
    
    def move(self, forward, dt):
        self.velocity = forward * PLAYER_SPEED * dt
        self.position -= self.velocity 
    
    def reset_velocity(self):
        self.velocity = pygame.Vector2(0, 0)

    def __repr__(self) -> str:
        return f"{self.position[0]}:{self.position[1]}"