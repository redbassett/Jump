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
        self.level = Level('reallevel')
        self.spawn()
        
        self.game_area = screen.subsurface((0, 40, screen.get_width(), screen.get_height() - 40))
        self.cam = Camera(self.player, self.level.bounds, self.game_area.get_size())
        
        self.hud = screen.subsurface((0, 0, screen.get_width(), 40))
        self.deathtext = pygame.font.Font(None, 20)


    def spawn(self):
        self.player = Player((self.level.spawnPoint), self.level, self)
        
            
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
                    self.player.jump()

            #update
            self.player.update(dt)
            self.cam.update(self.player.rect)

            #draw
            self.hud.fill((80, 80, 80))
            text = self.deathtext.render("deaths: " + str(self.deaths), True, (0, 255, 0)) 
        
            self.hud.blit(text, (0, 0))

            self.game_area.fill((0,0,0))
            self.cam.draw_background(self.game_area, self.level.background)
            self.cam.draw_sprite(self.game_area, self.player)

            #refresh
            pygame.display.flip()
