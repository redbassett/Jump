#!/usr/bin/env python

import pygame
from Player import *

class Game(object):
    done = False
    
    def __init__(self, screenSize):
        pygame.init()
        self.window = pygame.display.set_mode(screenSize)
        self.display = pygame.display
        self.display.set_caption('Jump')
        self.screen = self.display.get_surface()
        self.player = Player()
    
    def input(self, event):
        if event.type == pygame.QUIT:
            self.done = True
    
    def loop(self):
       while not self.done:
           #input
           for event in pygame.event.get():
                self.input(event)
                
           #update

           #draw
           self.screen.fill((0,0,0))
           self.player.draw(self.screen)
           
           #refresh
           self.display.flip()
