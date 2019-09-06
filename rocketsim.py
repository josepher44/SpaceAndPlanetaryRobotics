import pygame
from pygame.locals import *

#Basic loop structure from http://pygametutorials.wikidot.com/tutorials-basic

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.BLUE = (0,0,255)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((1600,800), pygame.HWSURFACE)
        self._running = True
        self._image_surf = pygame.image.load("kerbal.jpg").convert()



    #Detail definitions for three key loop elements

    #Event handler
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    #Loop definition
    def on_loop(self):
        pass
    def on_render(self):
        self._display_surf.blit(self._image_surf,(0,0))
        pygame.draw.rect(self._display_surf, self.BLUE,(200,200,20,199))
        #Refresh the full display
        pygame.display.flip()

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

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
