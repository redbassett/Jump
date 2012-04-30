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
        self.level = Level('testclip')
        self.players = [None, None]
        self.spawn(0)
        self.spawn(1)
        
        self.game_area = screen.subsurface((0, 40, screen.get_width(), screen.get_height() - 40))
        self.cam = Camera(self.players[0], self.level.bounds, self.game_area.get_size())
        
        self.hud = screen.subsurface((0, 0, screen.get_width(), 40))
    
    def spawn(self, index):
        if index == 0:
            color = (255, 255, 255)
            keys = (K_LEFT, K_RIGHT)
        else:
            color = (0, 0, 255)
            keys = (K_a, K_d)
        self.players[index] = Player((self.level.spawnPoint), self.level, self, index, keys, color)
            
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
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.players[0].jump()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    self.players[1].jump()

            #update
            for player in self.players:
                player.update(dt)
            #self.player.update(dt)
                self.cam.update(player.rect)

            #draw
            self.hud.fill((80, 80, 80))

            self.game_area.fill((0,0,0))
            self.cam.draw_background(self.game_area, self.level.background)
            for player in self.players:
                self.cam.draw_sprite(self.game_area, player)

            #refresh
            pygame.display.flip()
        if self.winner > -1:
            print 'Player #',(self.winner+1),' wins.'
