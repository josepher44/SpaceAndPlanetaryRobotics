import pygame
from pygame.locals import *

class asteroid:
    def __init__(self):
        self.RED = (255,0,0)
        self.color = None
        self.xpospixels = 100
        self.ypospixels = 400
        self.vspeed = 0
        self.hspeed = 32100

    def onloop(self, secondsperhour):
        print('Asteroid still exists!')
        #Convert km/h to pixels/step -- 30 steps per second, 10 seconds per real
        #hour, 160.5 kilometers per pixel
        self.hspeedpixels = self.hspeed*1.0/(140*30*secondsperhour)
        self.ypospixels = self.ypospixels+self.vspeed
        self.xpospixels = self.xpospixels+self.hspeedpixels
        print(self.xpospixels)

    def draw(self, surface):
        pygame.draw.circle(surface, self.RED,(int(round(self.xpospixels)),int(round(self.ypospixels))),5)
