import pygame
from pygame.locals import *

class asteroid:
    def __init__(self):
        self.RED = (255,0,0)
        self.color = None
        self.xpos = 300
        self.ypos = 400
        self.vspeed = 0
        self.hspeed = 32100

    def onloop(self):
        print('Asteroid still exists!')
        #Convert km/h to pixels/step -- 30 steps per second, 10 seconds per real
        #hour, 160.5 kilometers per pixel
        self.hspeedpixels = self.hspeed*1.0/(140*30*10)
        self.ypos = self.ypos+self.vspeed
        self.xpos = self.xpos+self.hspeedpixels
        print(self.xpos)

    def draw(self, surface):
        pygame.draw.circle(surface, self.RED,(int(round(self.xpos)),int(round(self.ypos))),5)
