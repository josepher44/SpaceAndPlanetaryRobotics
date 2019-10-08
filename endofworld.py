import pygame
from asteroid import *
from bomb import *
from pygame.locals import *

#Basic loop structure from http://pygametutorials.wikidot.com/tutorials-basic

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.asteroid = None
        self.bomb = None
        self.BLACK = (0,0,0)
        self.BLUE = (0,0,255)
        self.GRIDLINES = (80,80,80)
        self.clock = pygame.time.Clock()
        self.secondsperhour = 0
        self.tickcount = 0
        self.trigger = False

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((1600,800), pygame.HWSURFACE)
        self._running = True
        self._image_surf = pygame.image.load("kerbal.jpg").convert()
        self.asteroid = asteroid()
        self.bomb = bomb()
        self.secondsperhour = 10



    #Detail definitions for three key loop elements

    #Event handler
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    #Loop definition
    def on_loop(self):
        self.asteroid.onloop(self.secondsperhour)
        self.bomb.onloop(self.secondsperhour)
        self.clock.tick(30)
        pass
    def on_render(self):
        self._display_surf.fill(self.BLACK)
        for i in range(8):
            pygame.draw.line(self._display_surf, self.GRIDLINES, (1340-200*i,0),(1340-200*i,1000))
        pygame.draw.circle(self._display_surf, self.BLUE, (1340,400),40)
        self.asteroid.draw(self._display_surf)
        self.bomb.draw(self._display_surf)
        #Refresh the full display
        pygame.display.flip()

        self.tickcount = self.tickcount+1
        if self.tickcount>1500:
            self.tickcount=0
            self.asteroid = asteroid()
            self.bomb = bomb()
        if self.asteroid.xpospixels>self.bomb.xpospixels and self.trigger is False:
            self.trigger=True
            self.asteroid.acceleratefrombomb()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        #Main simulation loop -- follows event-loop-render design pattern
        while( self._running ):

            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

    def computedirectiontopoint(self, x1, y1, x2, y2):
        deltax = x1 - x2
        deltay = y1 - y2
        angle = math.atan(deltay/deltax)
        return angle

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
