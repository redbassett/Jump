#!/usr/bin/env python

import pygame
from Player import *

NORTH =(0, -1)
EAST = (1, 0)
SOUTH =(0, 1)
WEST = (-1, 0)

class Game(object):
    done = False
    
    def __init__(self, screenSize):
        pygame.init()
        self.window = pygame.display.set_mode(screenSize)
        self.display = pygame.display
        self.display.set_caption('Jump')
        self.screen = self.display.get_surface()
        self.spawn()
    
    def keyEval(self, key):
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.player.move(NORTH)
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.player.move(EAST)
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            self.player.move(SOUTH)
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            self.player.move(WEST)
    
    def input(self, event):
        if event.type == pygame.QUIT:
            self.done = True
        #elif event.type == pygame.KEYDOWN:
            #self.keyEval(event.key)
        #el

    
    def spawn(self):
        self.player = Player((0,0))
    
    def loop(self):
       while not self.done:
           #input
           if pygame.key.get_pressed()[pygame.K_UP]:
               self.player.move(NORTH)
           elif pygame.key.get_pressed()[pygame.K_RIGHT]:
               self.player.move(EAST)
           elif pygame.key.get_pressed()[pygame.K_DOWN]:
               self.player.move(SOUTH)
           elif pygame.key.get_pressed()[pygame.K_LEFT]:
               self.player.move(WEST)

           #update

           #draw
           self.screen.fill((0,0,0))
           self.player.draw(self.screen)
           
           #refresh
           self.display.flip()
