import pygame
import math
from pygame.locals import *

class bomb:
    def __init__(self):
        self.GREEN = (0,255,0)
        self.color = None
        self.xpospixels = 1340
        self.ypospixels = 360
        self.vspeed = 0
        self.hspeed = -40000
        self.angle = 0

    def onloop(self, secondsperhour):
        #print('Bomb still exists!')
        #Convert km/h to pixels/step -- 30 steps per second, 10 seconds per real
        #hour, 160.5 kilometers per pixel
        self.angle=self.angle+0.01
        self.hspeed = self.componentsfromheading(self.angle)[0]
        self.vspeed = self.componentsfromheading(self.angle)[1]
        self.hspeedpixels = self.hspeed*1.0/(140*30*secondsperhour)
        self.vspeedpixels = self.vspeed*1.0/(140*30*secondsperhour)
        self.ypospixels = self.ypospixels+self.vspeedpixels
        self.xpospixels = self.xpospixels+self.hspeedpixels
        #print(self.xpos)

    def draw(self, surface):
        pygame.draw.circle(surface, self.GREEN,(int(round(self.xpospixels)),int(round(self.ypospixels))),2)

    def componentsfromheading(self, angle):
        horizontal = -40000*math.cos(angle)
        vertical = 40000*math.sin(angle)
        return(horizontal, vertical)
