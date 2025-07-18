from circleshape import *
from Space.shoot import *
from Planet.shoot import *
from constants import PLAYER_CONSTANTS, SCREEN_WIDTH, SCREEN_HEIGHT


class Space_Player(Character):
    def __init__(self, x, y, l = None, e = 0, score = 0):
        super().__init__(x, y, score, PLAYER_CONSTANTS["ship"]["radius"])
        self.__level = {"rate_of_fire": (1, 5), 
                      "ship_speed": (1, 3),
                      "projectile_num": (1, 3),
                      "directions": (1, 3), 
                      }
        if l:
            self.__level = l
        self.exp = e
        self.dead = False
        self.__shoot_timer = 0
        self.bullets = self.__level["projectile_num"][0]

    def get_level(self):
        return self.__level
    
    def level_up(self, level):
        print(level, self.__level[level][0])
        self.__level[level] = (self.__level[level][0]+1, self.__level[level][1])
        print(level, self.__level[level][0])

    def revive(self):
        self.dead = False
        self.score = 0

    def change_player(self):
        print("from space to planet")
        return Planet_Player(300, SCREEN_HEIGHT/2, self.__level, self.exp, self.score)
    
    def draw(self, screen):
        pygame.draw.polygon(screen, 'white', self.triangle(), width=2)

    def drawStats(self, screen):
        font = pygame.font.SysFont('arial', 16)

        i = 1
        for item in self.__level.items():
            text_surface = font.render(f"{item[0]}: lvl {item[1]}", True, (255, 255, 255))
            screen.blit(text_surface, (1200 - text_surface.get_width(), i*20))
            i += 1

        text_surface = font.render(f"current score: {self.score}", True, (255, 255, 255))
        screen.blit(text_surface, (1200 - text_surface.get_width(), i*20))

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]    

    def rotate(self, dt):
        self.rotation += PLAYER_CONSTANTS["ship"]["turn_speed"]*dt    

    def update(self, dt, camera):
        keys = pygame.key.get_pressed()
        speed = PLAYER_CONSTANTS["ship"]["speed"][self.__level["ship_speed"][0]-1]
        if self.__shoot_timer > 0:
            self.__shoot_timer -= dt
        else:
            self.__shoot_timer = 0
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            camera.move(pygame.Vector2(0, 1).rotate(self.rotation) * speed, dt)
        elif keys[pygame.K_s]:
            camera.move(pygame.Vector2(0, 1).rotate(self.rotation) * speed, -dt)
        else: camera.reset_velocity()
        if pygame.mouse.get_pressed(num_buttons=5)[0]:
            self.space_shoot()
            
        if self.bullets != self.__level["projectile_num"][0]:
            self.space_shoot()
     
    def space_shoot(self):
        if self.__shoot_timer == 0:
            match self.__level["directions"][0]:
                case 1:
                    bullet = Space_Shoot(self.position.x, self.position.y)
                    bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation)*PLAYER_CONSTANTS["weapon"]["projectile"]["speed"]
            
                case 2:
                    bullet1 = Space_Shoot(self.position.x, self.position.y)
                    bullet1.velocity = pygame.Vector2(0, 1).rotate(self.rotation+20)*PLAYER_CONSTANTS["weapon"]["projectile"]["speed"]
            
                    bullet2 = Space_Shoot(self.position.x, self.position.y)
                    bullet2.velocity = pygame.Vector2(0, 1).rotate(self.rotation-20)*PLAYER_CONSTANTS["weapon"]["projectile"]["speed"]
            
                case 3:
                    bullet1 = Space_Shoot(self.position.x, self.position.y)
                    bullet1.velocity = pygame.Vector2(0, 1).rotate(self.rotation)*PLAYER_CONSTANTS["weapon"]["projectile"]["speed"]
                    
                    bullet2 = Space_Shoot(self.position.x, self.position.y)
                    bullet2.velocity = pygame.Vector2(0, 1).rotate(self.rotation+20)*PLAYER_CONSTANTS["weapon"]["projectile"]["speed"]
                    
                    bullet3 = Space_Shoot(self.position.x, self.position.y)
                    bullet3.velocity = pygame.Vector2(0, 1).rotate(self.rotation-20)*PLAYER_CONSTANTS["weapon"]["projectile"]["speed"]
            
            self.__shoot_timer = PLAYER_CONSTANTS["weapon"]["rate_of_fire"][self.__level["rate_of_fire"][0]-1]
            self.bullets -= 1
            if self.bullets > 0:
                self.__shoot_timer = 0.02
            else:
                self.bullets = self.__level["projectile_num"][0]




class Planet_Player(Character):
    def __init__(self, x, y, l, e, score = 0):
        super().__init__(x, y, score, PLAYER_CONSTANTS["ship"]["radius"])
        self.__level = l
        self.exp = e
        self.dead = False
        self.__shoot_timer = 0
        self.bullets = self.__level["projectile_num"][0]

    def change_player(self):
        print("from planet to space")
        return Space_Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, self.__level, self.exp, self.score)
    
    def draw(self, screen):
        pygame.draw.polygon(screen, 'white', self.triangle(), width=2)

    def drawStats(self, screen):
        font = pygame.font.SysFont('arial', 16)

        i = 1
        for item in self.__level.items():
            text_surface = font.render(f"{item[0]}: lvl {item[1]}", True, (255, 255, 255))
            screen.blit(text_surface, (1200 - text_surface.get_width(), i*20))
            i += 1
       
        text_surface = font.render(f"current score: {self.score}", True, (255, 255, 255))
        screen.blit(text_surface, (1200 - text_surface.get_width(), i*20))

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]    

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.__shoot_timer > 0:
            self.__shoot_timer -= dt
        else:
            self.__shoot_timer = 0
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
        if self.bullets != self.__level["projectile_num"][0]:
            self.planet_shoot()
        
    def move(self, forward, dt):
        self.velocity = forward * PLAYER_CONSTANTS["ship"]["speed"][self.__level["ship_speed"][0]-1] * dt
        self.position += self.velocity 
    
    def planet_shoot(self):
        if self.__shoot_timer == 0:
            match self.__level["directions"][0]:
                case 1:
                    bullet = Planet_Shoot(self.position.x+self.radius+PLAYER_CONSTANTS["weapon"]["projectile"]["radius"], self.position.y, PLAYER_CONSTANTS["weapon"]["projectile"]["radius"], True)
                    bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation)*PLAYER_CONSTANTS["weapon"]["projectile"]["speed"]
            
                case 2:
                    bullet1 = Planet_Shoot(self.position.x+self.radius+PLAYER_CONSTANTS["weapon"]["projectile"]["radius"], self.position.y, PLAYER_CONSTANTS["weapon"]["projectile"]["radius"], True)
                    bullet1.velocity = pygame.Vector2(0, 1).rotate(self.rotation+20)*PLAYER_CONSTANTS["weapon"]["projectile"]["speed"]
            
                    bullet2 = Planet_Shoot(self.position.x+self.radius+PLAYER_CONSTANTS["weapon"]["projectile"]["radius"], self.position.y, PLAYER_CONSTANTS["weapon"]["projectile"]["radius"], True)
                    bullet2.velocity = pygame.Vector2(0, 1).rotate(self.rotation-20)*PLAYER_CONSTANTS["weapon"]["projectile"]["speed"]
            
                case 3:
                    bullet1 = Planet_Shoot(self.position.x+self.radius+PLAYER_CONSTANTS["weapon"]["projectile"]["radius"], self.position.y, PLAYER_CONSTANTS["weapon"]["projectile"]["radius"], True)
                    bullet1.velocity = pygame.Vector2(0, 1).rotate(self.rotation)*PLAYER_CONSTANTS["weapon"]["projectile"]["speed"]
                    
                    bullet2 = Planet_Shoot(self.position.x+self.radius+PLAYER_CONSTANTS["weapon"]["projectile"]["radius"], self.position.y, PLAYER_CONSTANTS["weapon"]["projectile"]["radius"], True)
                    bullet2.velocity = pygame.Vector2(0, 1).rotate(self.rotation+20)*PLAYER_CONSTANTS["weapon"]["projectile"]["speed"]
                    
                    bullet3 = Planet_Shoot(self.position.x+self.radius+PLAYER_CONSTANTS["weapon"]["projectile"]["radius"], self.position.y, PLAYER_CONSTANTS["weapon"]["projectile"]["radius"], True)
                    bullet3.velocity = pygame.Vector2(0, 1).rotate(self.rotation-20)*PLAYER_CONSTANTS["weapon"]["projectile"]["speed"]
            
            self.__shoot_timer = PLAYER_CONSTANTS["weapon"]["rate_of_fire"][self.__level["rate_of_fire"][0]-1]
            self.bullets -= 1
            if self.bullets > 0:
                self.__shoot_timer = 0.02
            else:
                self.bullets = self.__level["projectile_num"][0]
    
    def collsion(self, other):
        if not other.friendly:
            return super().collsion(other)
        return False
   