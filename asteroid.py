import pygame
import math
from pygame.locals import *

class asteroid:
    def __init__(self):
        self.RED = (255,0,0)
        self.color = None
        self.xpos = -192600-6536
        self.ypos = 0
        self.xpospixels = 100
        self.ypospixels = 250
        self.vspeed = 0
        self.hspeed = 32100
        self.xaccel = 0
        self.yaccel = 0
        self.loopcount=0
        self.trigger = False

    def onloop(self, secondsperhour):
        #print('Asteroid still exists!')
        #Convert km/h to pixels/step -- 30 steps per second, 10 seconds per real
        #hour, 160.5 kilometers per pixel
        print(self.computedirectiontopoint(0,0))
        self.hspeed = self.hspeed + self.applyacceleration(0.1,self.computedirectiontopoint(0,0))[0]
        self.vspeed = self.vspeed + self.applyacceleration(0.1,self.computedirectiontopoint(0,0))[1]
        if self.trigger:
            self.hspeed = self.hspeed+self.applyacceleration(50,-math.pi/2)[0]
            self.vspeed = self.vspeed+self.applyacceleration(50,-math.pi/2)[1]
            self.trigger=False
        self.xpos = self.xpos + self.hspeed/(10*30)
        self.ypos = self.ypos + self.vspeed/(10*30)
        self.xpospixels = self.xpos/160.5 + 1340
        self.ypospixels = self.ypos/160.5 + 400
        #self.hspeedpixels = self.hspeed*1.0/(140*30*secondsperhour)
        #self.vspeedpixels = self.vspeed*1.0/(140*30*secondsperhour)
        #self.xpospixels = self.xpospixels+self.hspeedpixels
        self.loopcount=self.loopcount+1
        if self.loopcount is 10:
            self.loopcount=0
            print(self.xpos)

    def acceleratefrombomb(self):
        self.trigger = True

    def draw(self, surface):
        pygame.draw.circle(surface, self.RED,(int(round(self.xpospixels)),int(round(self.ypospixels))),5)

    def computedirectiontopoint(self, x, y):
        deltax = self.xpos - x
        deltay = self.ypos - y
        angle = math.atan(deltay/deltax)
        return angle

    #Returns the changes to the horizontal
    def applyacceleration(self, magnitude, direction):
        return (magnitude*math.cos(direction)*100, magnitude*math.sin(direction)*100)
