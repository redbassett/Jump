#!/usr/bin/env python

import pygame
from Player import *

NORTH =(0, -1)
EAST = (1, 0)
SOUTH =(0, 1)
WEST = (-1, 0)

class Game(object):
    
    def __init__(self, screenSize):
        pygame.init()
        self.screen = pygame.display.set_mode(screenSize)
        pygame.display.set_caption('Jump')
        self.spawn()
    
    
    def spawn(self):
        self.player = Player((50,50))
    
    def loop(self):
        self.done = False
        self.clock = pygame.time.Clock()
        while not self.done:
            dt = self.clock.tick(30)

            #input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.done = True

            #update
            self.player.update(dt)

            #draw
            self.screen.fill((0,0,0))
            self.screen.blit(self.player.image, self.player.rect)
             
            #refresh
            pygame.display.flip()
