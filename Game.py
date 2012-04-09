#!/usr/bin/env python

import pygame
from pygame.sprite import Group
from Player import *
from Block import *

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
        self.blocks = Group()
        self.blocks.add(Block((100,100)))
    
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
            self.blocks.update()

            #draw
            self.screen.fill((0,0,0))
            self.screen.blit(self.player.image, self.player.rect)
            self.blocks.draw(self.screen) 

            #refresh
            pygame.display.flip()
