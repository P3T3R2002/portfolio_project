import pygame
from constants import *
from circleshape import *

class BST_Map_Node(CircleShape):
    def __init__(self, dif=1, num = 0):
        super().__init__(-MAP_WIDTH/(2**(dif-1)+1)*(num+1) + MAP_WIDTH/2, -(MAP_HIGHT-1000)/4*dif, 200)
        self.start_pos = pygame.Vector2(self.position.x, self.position.y)
        self.left = None
        self.right = None
        self.completed = False
        self.difficulty = dif
        if self.difficulty == 1:
            self.available = True
        else:
            self.available = False
        self.__generate_map(4, num)

    def __generate_map(self, max_diff, num):
        if self.difficulty == max_diff:
            return
        self.left = BST_Map_Node(self.difficulty+1, num*2)
        self.right = BST_Map_Node(self.difficulty+1, num*2+1)

    def completed_Node(self): 
        self.completed = True
        if self.left:
            self.left.available = True
        if self.right:
            self.right.available = True

    def draw(self, screen):
        color = None
        if self.completed:
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
        print(pos)
        color = None
        if self.completed:
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
        
    def update(self, dt, camera):
        self.position += self.velocity*dt - camera.velocity
        if self.left:
            self.left.update(dt, camera)
        if self.right:
            self.right.update(dt, camera)



