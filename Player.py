#!/usr/bin/env python

import pygame
"""
A player is a character in the game.  All players are human controlled.
"""
class Player(object):
    def __init__(self, color = (255,255,255)):
        self.x, self.y  = (0,0)
        self.w, self.h = (20,20)
        self.color = color
    
    def draw(self, screen):
        rect = pygame.Rect((self.x, self.y), (self.w, self.h))
        pygame.draw.rect(screen, self.color, rect)
