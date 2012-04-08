#!/usr/bin/env python

import pygame

class Game(object):
    done = False
    
    def __init__(self, screenSize):
        pygame.init()
        self.window = pygame.display.set_mode(screenSize)
        pygame.display.set_caption('Jump')
        self.screen = pygame.display.get_surface()
    
    def input(self, event):
        if event.type == pygame.QUIT:
            self.done = True
    
    def loop(self):
       while not self.done:
            for event in pygame.event.get():
                self.input(event)
