#!/usr/bin/env python

from pygame.locals import *
from overloading import overload

class def Game(object):
    def __init__(self, screenSize):
        pygame.init()
        self.window = pygame.display.set_mode(screenSize)
        self.display.set_caption('Jump')
        self.screen = pygame.display.get_surface()
    
    def input(self, event):
        if event.type == QUIT:
            self.done = False
    
    def loop(self):
        while not done:
            pass # Game loop here
