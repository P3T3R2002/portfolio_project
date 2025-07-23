from hud import HUD
from circleshape import *
from Space.shoot import *
from Planet.shoot import *
from constants import PLAYER_CONSTANTS, SCREEN_WIDTH, SCREEN_HEIGHT


class Space_Player(Character):
    def __init__(self, x, y, l = None, e = 0, score = 0):
        super().__init__(x, y, score, PLAYER_CONSTANTS["ship"]["radius"], PLAYER_CONSTANTS["ship"]["source"])
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
        self.image = pygame.transform.rotate(self.image, -90)

    def get_level(self):
        return self.__level
    
    def level_up(self, level):
        self.__level[level] = (self.__level[level][0]+1, self.__level[level][1])

    def revive(self):
        self.dead = False
        self.score = 0

    def change_player(self):
        print("from space to planet")
        return Planet_Player(300, SCREEN_HEIGHT/2, self.__level, self.exp, self.score)
    
    def rotate(self, dt):
        self.rotation += PLAYER_CONSTANTS["ship"]["turn_speed"]*dt   
        self.image = pygame.transform.rotate(PLAYER_CONSTANTS["ship"]["source"], -self.rotation+90) 
        self.image_rect = self.image.get_rect(center=self.position)

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
                    bullet = Space_Shoot(self.position.x, self.position.y, self.rotation)
                    bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation)*PLAYER_CONSTANTS["weapon"]["projectile"]["speed"]
            
                case 2:
                    bullet1 = Space_Shoot(self.position.x, self.position.y, self.rotation+10)
                    bullet1.velocity = pygame.Vector2(0, 1).rotate(self.rotation+10)*PLAYER_CONSTANTS["weapon"]["projectile"]["speed"]
            
                    bullet2 = Space_Shoot(self.position.x, self.position.y, self.rotation-10)
                    bullet2.velocity = pygame.Vector2(0, 1).rotate(self.rotation-10)*PLAYER_CONSTANTS["weapon"]["projectile"]["speed"]
            
                case 3:
                    bullet1 = Space_Shoot(self.position.x, self.position.y, self.rotation)
                    bullet1.velocity = pygame.Vector2(0, 1).rotate(self.rotation)*PLAYER_CONSTANTS["weapon"]["projectile"]["speed"]
                    
                    bullet2 = Space_Shoot(self.position.x, self.position.y, self.rotation+20)
                    bullet2.velocity = pygame.Vector2(0, 1).rotate(self.rotation+20)*PLAYER_CONSTANTS["weapon"]["projectile"]["speed"]
                    
                    bullet3 = Space_Shoot(self.position.x, self.position.y, self.rotation-20)
                    bullet3.velocity = pygame.Vector2(0, 1).rotate(self.rotation-20)*PLAYER_CONSTANTS["weapon"]["projectile"]["speed"]
            
            self.__shoot_timer = PLAYER_CONSTANTS["weapon"]["rate_of_fire"][self.__level["rate_of_fire"][0]-1]
            self.bullets -= 1
            if self.bullets > 0:
                self.__shoot_timer = 0.02
            else:
                self.bullets = self.__level["projectile_num"][0]




class Planet_Player(Character):
    def __init__(self, x, y, l, e, score = 0):
        super().__init__(x, y, score, PLAYER_CONSTANTS["ship"]["radius"], PLAYER_CONSTANTS["ship"]["source"])
        self.__level = l
        self.exp = e
        self.dead = False
        self.__shoot_timer = 0
        self.bullets = self.__level["projectile_num"][0]
        self.rotation = 270
        self.image = pygame.transform.rotate(self.image, 180)

    def get_level(self):
        return self.__level
    
    def change_player(self):
        print("from planet to space")
        return Space_Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, self.__level, self.exp, self.score)
    
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
        self.image_rect.center = self.position
    
    def planet_shoot(self):
        if self.__shoot_timer == 0:
            match self.__level["directions"][0]:
                case 1:
                    bullet = Planet_Shoot(self.position.x+self.radius+PLAYER_CONSTANTS["weapon"]["projectile"]["radius"], self.position.y, True, self.rotation)
                    bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation)*PLAYER_CONSTANTS["weapon"]["projectile"]["speed"]
            
                case 2:
                    bullet1 = Planet_Shoot(self.position.x+self.radius+PLAYER_CONSTANTS["weapon"]["projectile"]["radius"], self.position.y, True, self.rotation+10)
                    bullet1.velocity = pygame.Vector2(0, 1).rotate(self.rotation+10)*PLAYER_CONSTANTS["weapon"]["projectile"]["speed"]
            
                    bullet2 = Planet_Shoot(self.position.x+self.radius+PLAYER_CONSTANTS["weapon"]["projectile"]["radius"], self.position.y, True, self.rotation-10)
                    bullet2.velocity = pygame.Vector2(0, 1).rotate(self.rotation-10)*PLAYER_CONSTANTS["weapon"]["projectile"]["speed"]
            
                case 3:
                    bullet1 = Planet_Shoot(self.position.x+self.radius+PLAYER_CONSTANTS["weapon"]["projectile"]["radius"], self.position.y, True, self.rotation)
                    bullet1.velocity = pygame.Vector2(0, 1).rotate(self.rotation)*PLAYER_CONSTANTS["weapon"]["projectile"]["speed"]
                    
                    bullet2 = Planet_Shoot(self.position.x+self.radius+PLAYER_CONSTANTS["weapon"]["projectile"]["radius"], self.position.y, True, self.rotation+20)
                    bullet2.velocity = pygame.Vector2(0, 1).rotate(self.rotation+20)*PLAYER_CONSTANTS["weapon"]["projectile"]["speed"]
                    
                    bullet3 = Planet_Shoot(self.position.x+self.radius+PLAYER_CONSTANTS["weapon"]["projectile"]["radius"], self.position.y, True, self.rotation-20)
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
   