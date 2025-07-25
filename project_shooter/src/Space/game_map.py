import pygame
from constants import MAP_WIDTH, MAP_HIGHT, PLANET_CONSTANTS
from circleshape import *
from Planet.planet_map import *

class BST_Map_Node(CircleShape):
    def __init__(self, dif=1, num = 0):
        super().__init__(-MAP_WIDTH/(2**(dif-1)+1)*(num+1) + MAP_WIDTH/2, -(MAP_HIGHT-1000)/4*dif, PLANET_CONSTANTS['radius'], PLANET_CONSTANTS['source'])
        self.start_pos = pygame.Vector2(self.position.x, self.position.y)
        self.left = None
        self.right = None
        self.val = Planet(dif)
        if dif == 1:
            self.available = True
        else:
            self.available = False
        self.__generate_map(4, num)
        
        self.circle_surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
    

    def __generate_map(self, max_diff, num):
        dif = self.val.get_difficulty()
        if dif == max_diff:
            return
        self.left = BST_Map_Node(dif+1, num*2)
        self.right = BST_Map_Node(dif+1, num*2+1)

    def completed_Node(self, planet): 
        if self.val == planet:
            self.available = False
            if self.left:
                self.left.available = True
            if self.right:
                self.right.available = True
        else:
            if self.left:
                self.left.completed_Node(planet)
            if self.right:
                self.right.completed_Node(planet)

    def draw(self, screen):
        screen.blit(self.image, self.image_rect)
        if self.val.get_completion():
            color = (0, 255, 0, 100)
            pygame.draw.circle(self.circle_surface, color, (self.radius, self.radius), self.radius)
            screen.blit(self.circle_surface, (self.position[0] - self.radius, self.position[1] - self.radius))
        elif not self.available:
            color = (255, 0, 0, 100)
            pygame.draw.circle(self.circle_surface, color, (self.radius, self.radius), self.radius)
            screen.blit(self.circle_surface, (self.position[0] - self.radius, self.position[1] - self.radius))

        if self.left:
            self.left.draw(screen)
        if self.right:
            self.right.draw(screen)
   
        
    def collsion(self, other):
        if super().collsion(other):
            if self.available:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    print("OK")
                    return self.val
        
        if self.left:
            planet =  self.left.collsion(other)
            if planet:
                return planet
        if self.right:
            planet = self.right.collsion(other)
            if planet:
                return planet
        return None
      
    def update(self, dt, camera):
        self.position += self.velocity*dt - camera.velocity
        self.image_rect.center = self.position

        winner1 = False
        winner2 = False
        if self.left:
            winner1 = self.left.update(dt, camera)
        else:
            winner1 = self.val.get_completion()
        if self.right:
            winner2 = self.right.update(dt, camera)
        else:
            winner2 = self.val.get_completion()
        if winner2 and winner1:
            return True
        return False
         


