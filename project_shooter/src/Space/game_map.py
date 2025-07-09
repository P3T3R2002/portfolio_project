import pygame
from constants import *
from circleshape import *
from Planet.planet_map import *

class BST_Map_Node(CircleShape):
    def __init__(self, dif=1, num = 0):
        super().__init__(-MAP_WIDTH/(2**(dif-1)+1)*(num+1) + MAP_WIDTH/2, -(MAP_HIGHT-1000)/4*dif, 200)
        self.start_pos = pygame.Vector2(self.position.x, self.position.y)
        self.left = None
        self.right = None
        self.val = Planet(dif)
        if dif == 1:
            self.available = True
        else:
            self.available = False
        self.__generate_map(4, num)

    def __generate_map(self, max_diff, num):
        if self.val.difficulty == max_diff:
            return
        self.left = BST_Map_Node(self.val.difficulty+1, num*2)
        self.right = BST_Map_Node(self.val.difficulty+1, num*2+1)

    def completed_Node(self, planet): 
        if self.val == planet:
            self.available = False
            if self.left:
                self.left.available = True
            if self.right:
                self.right.available = True
        else:
            self.left.completed_Node(planet)
            self.right.completed_Node(planet)

    def draw(self, screen):
        color = None
        if self.val.completed:
            color = 'Green'
        elif self.available:
            color = 'Blue'
        else:
            color = 'Red'
        pygame.draw.circle(screen, color, self.position, self.radius)
        if self.left:
            self.left.draw(screen)
        if self.right:
            self.right.draw(screen)

    def draw_minimap(self, screen):
        pygame.draw.rect(screen, "yellow", pygame.Rect((0, 0), (200, 100)), 2)
        pos = ((self.start_pos.x + MAP_WIDTH/2)/100, (self.start_pos.y + (MAP_HIGHT+200))/100)
        color = None
        if self.val.completed:
            color = 'Green'
        elif self.available:
            color = 'Blue'
        else:
            color = 'Red'
        pygame.draw.circle(screen, color, pos, 3)
        if self.left:
            self.left.draw_minimap(screen)
        if self.right:
            self.right.draw_minimap(screen)     
        
    def collsion(self, other):
        if super().collsion(other):
            if self.available:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    self.completed_Node()
                    return self
        
        if self.left:
            return self.left.collsion(other)
        if self.right:
            return self.right.collsion(other)
        return None
      
    def update(self, dt, camera):
        self.position += self.velocity*dt - camera.velocity

        winner1 = False
        winner2 = False
        if self.left:
            winner1 = self.left.update(dt, camera)
        else:
            winner1 = self.val.completed
        if self.right:
            winner2 = self.right.update(dt, camera)
        else:
            winner2 = self.val.completed
        if winner2 and winner1:
            return True
        return False
         



