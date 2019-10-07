import pygame
from pygame.locals import *

class bomb:
    def __init__(self):
        self.GREEN = (0,255,0)
        self.color = None
        self.xpos = 1340
        self.ypos = 360
        self.vspeed = 0
        self.hspeed = -40000

    def onloop(self, secondsperhour):
        print('Bomb still exists!')
        #Convert km/h to pixels/step -- 30 steps per second, 10 seconds per real
        #hour, 160.5 kilometers per pixel
        self.hspeedpixels = self.hspeed*1.0/(140*30*secondsperhour)
        self.ypos = self.ypos+self.vspeed
        self.xpos = self.xpos+self.hspeedpixels
        print(self.xpos)

    def draw(self, surface):
        pygame.draw.circle(surface, self.GREEN,(int(round(self.xpos)),int(round(self.ypos))),2)
