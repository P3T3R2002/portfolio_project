from circleshape import *
from constants import *

class Planet_Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.score = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, 'white', self.triangle(), width=2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]    

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED*dt    

    def update(self, dt, camera):
        keys = pygame.key.get_pressed()
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
        else:
            self.shoot_timer = 0
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            camera.move(pygame.Vector2(0, 1).rotate(self.rotation), dt)
        elif keys[pygame.K_s]:
            camera.move(pygame.Vector2(0, 1).rotate(self.rotation), -dt)
        else: camera.reset_velocity()
        if pygame.mouse.get_pressed(num_buttons=5)[0]:
            self.shoot()
        

    def shoot(self):
        if self.shoot_timer == 0:
            bullet = Shoot(self.position[0], self.position[1])
            bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation)*PLAYER_SHOOT_SPEED
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN

class Shoot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width=2)
        
    def update(self, dt, _):
        self.position += self.velocity*dt

    