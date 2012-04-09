#!/usr/bin/env python

import pygame
from pygame.sprite import Group
from Player import *
from Block import *
from Camera import *
from Level import *

NORTH =(0, -1)
EAST = (1, 0)
SOUTH =(0, 1)
WEST = (-1, 0)

class Game(object):
    
    def __init__(self, screen):
        self.deaths = 0
        
        self.screen = screen
        self.level = Level()
        self.spawn()

        #self.cam = Camera(self.player, self.level.bounds, self.game_area.get_size())
        

        # self.hud = screen.subsurface((0, 0, screen.get_width(), 40))
        # self.game_area = screen.subsurface((0, 40, screen.get_width(), screen.get_height() - 40))
        #How do we use this? It needs to display deaths
    
    
    def spawn(self):
        self.player = Player((self.level.spawnPoint), self.level, self)
        print self.deaths
            
    def quit(self):
        self.done = True
    
    def loop(self):
        self.done = False
        self.clock = pygame.time.Clock()
        while not self.done:
            dt = self.clock.tick(30)

            #input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.quit()

            #update
            self.player.update(dt)
           
            #for collide in spritecollide(self.player, self.lethal, True):
             #   self.deaths += 1
            #This needs to also be set to restart the player in its original position.

            #draw
            self.screen.fill((0,0,0))
            self.screen.blit(self.player.image, self.player.rect)

            #refresh
            pygame.display.flip()
