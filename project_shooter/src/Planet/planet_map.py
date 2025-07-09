import pygame
from constants import *
from circleshape import *

class Planet:
    def __init__(self, dif=1):
        self.completed = False
        self.difficulty = dif
