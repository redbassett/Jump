#!/usr/bin/env python

import pygame
"""
A player is a character in the game.  All players are human controlled.
"""

class Player(object):
    def __init__(self, (x,y), color = (255,255,255), (w,h) = (20,20)):
        self.x, self.y  = (x,y)
        self.w, self.h = (w,h)
        self.color = color
    
    def draw(self, screen):
        rect = pygame.Rect((self.x, self.y), (self.w, self.h))
        pygame.draw.rect(screen, self.color, rect)
    
    def move(self, (x, y)):
        self.x += x
        self.y += y
