import pygame
import random
from constants import ASTEROID_CONSTANTS, SCREEN_WIDTH, SCREEN_HEIGHT
from Space.asteroid import Asteroid


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2((-ASTEROID_CONSTANTS['max_radius'], y * SCREEN_HEIGHT)),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2((SCREEN_WIDTH + ASTEROID_CONSTANTS['max_radius'], y * SCREEN_HEIGHT)),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2((x * SCREEN_WIDTH, -ASTEROID_CONSTANTS['max_radius'])),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2((x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_CONSTANTS['max_radius'])),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity, url):
        asteroid = Asteroid(position.x, position.y, radius, url)
        asteroid.velocity = velocity

    def update(self, dt, _):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_CONSTANTS['spawn_rate']:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_CONSTANTS['kinds']["num"])
            url = None
            match kind:
                case 1: url = ASTEROID_CONSTANTS['kinds']["SMALL"]
                case 2: url = ASTEROID_CONSTANTS['kinds']["MIDDLE"]
                case 3: url = ASTEROID_CONSTANTS['kinds']["BIG"]
                
            self.spawn(ASTEROID_CONSTANTS['min_radius'] * kind, position, velocity, url)
