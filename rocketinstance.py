import pygame
from pygame.locals import *

class rocket:
    def __init__(self):
        self.BLUE = (0,0,255)
        self.RED = (255,0,0)
        self.color = None
        self.xpos = 300
        self.ypos = 0
        self.vspeed = 0
        print('Rocket exists!')

    def onloop(self):
        print('Rocket still exists!')
        self.vspeed = self.vspeed+0.002
        self.ypos = self.ypos+self.vspeed

    def draw(self, surface):
        if self.ypos>400:
            self.color = self.RED;
        else:
            self.color = self.BLUE;
        pygame.draw.rect(surface, self.color,(self.xpos,self.ypos,20,199))
