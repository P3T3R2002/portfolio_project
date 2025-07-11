from circleshape import *
from constants import *

class Character(CircleShape):
    def __init__(self, x, y, score, r = PLAYER_RADIUS):
        super().__init__(x, y, r)
        self.rotation = 270
        self.shoot_timer = 0
        self.score = score

class Space_Player(Character):
    def __init__(self, x, y, score = 0):
        super().__init__(x, y, score)
        self.shoot_timer = 0

    def change_player(self):
        return Planet_Player(300, SCREEN_HEIGHT/2, self.score)

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
            self.space_shoot()
        

    def space_shoot(self):
        if self.shoot_timer == 0:
            bullet = Space_Shoot(self.position[0], self.position[1])
            bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation)*PLAYER_SHOOT_SPEED
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN

class Planet_Player(Character):
    def __init__(self, x, y, score = 0):
        super().__init__(x, y, score)
        self.shoot_timer = 0

    def change_player(self):
        return Space_Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, self.score)
    
    def draw(self, screen):
        pygame.draw.polygon(screen, 'white', self.triangle(), width=2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]    

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
        else:
            self.shoot_timer = 0
        if keys[pygame.K_a]:
            self.move(pygame.Vector2(-1, 0), dt)
        if keys[pygame.K_d]:
            self.move(pygame.Vector2(1, 0), dt)
        if keys[pygame.K_w]:
            self.move(pygame.Vector2(0, -1), dt)
        elif keys[pygame.K_s]:
            self.move(pygame.Vector2(0, 1), dt)
        if pygame.mouse.get_pressed(num_buttons=5)[0]:
            self.planet_shoot()
        
    def move(self, forward, dt):
        self.velocity = forward * PLAYER_SPEED * dt
        self.position += self.velocity 
    
    def planet_shoot(self):
        if self.shoot_timer == 0:
            bullet = Planet_Shoot(self.position.x+self.radius+PLAYER_SHOT_RADIUS, self.position.y, PLAYER_SHOT_RADIUS, True)
            bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation)*PLAYER_SHOOT_SPEED
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN
    
    def collsion(self, other):
        if not other.friendly:
            return super().collsion(other)
        return False
    
class Enemy(Character):
    def __init__(self, x, y, r, score = 0):
        super().__init__(x, y, score, r)
        self.shoot_timer = 0
    
    def draw(self, screen):
        pygame.draw.polygon(screen, 'RED', self.triangle(), width=2)

    def triangle(self):
        forward = pygame.Vector2(-1, 0)
        right = pygame.Vector2(0, -1) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]    

    def update(self, dt):
        self.move(dt)
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
        else:
            self.shoot_timer = 0
        self.planet_shoot()
        
    def move(self, dt):
        self.position += self.velocity * dt
    
    def planet_shoot(self):
        if self.shoot_timer == 0:
            bullet = Planet_Shoot(self.position.x-self.radius-ENEMY_SHOT_RADIUS, self.position.y, ENEMY_SHOT_RADIUS, False)
            bullet.velocity = pygame.Vector2(-1, 0)*ENEMY_SHOOT_SPEED
            self.shoot_timer = ENEMY_SHOOT_COOLDOWN

    def collsion(self, other):
        if other.friendly:
            return super().collsion(other)
        return False

class Space_Shoot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_SHOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width=2)
        
    def update(self, dt, camera):
        self.position += self.velocity*dt - camera.velocity

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
    