import pygame
from pygame.locals import *

class rocket:
    def __init__(self):
        self.BLUE = (0,0,255)
        print('Rocket exists!')

    def onloop(self):
        print('Rocket still exists!')

    def draw(self, surface):
        pygame.draw.rect(surface, self.BLUE,(200,200,20,199))
