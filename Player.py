#!/usr/bin/env python

import pygame
from pygame.locals import *
from pygame.sprite import Sprite
"""
A player is a character in the game.  All players are human controlled.
"""

PLAYER_SPEED = 240

class Player(Sprite):
    def __init__(self, (x,y), color = (255,255,255), (w,h) = (20,20)):
        Sprite.__init__(self)
        self.x, self.y  = (x,y)
        
        self.image = pygame.Surface((w,h))
        self.rect = self.image.get_rect()
        self.rect.topleft = x,y

        self.image.fill(color)

        self.vx = 0
        self.vy = 0

    def update(self, dt):
        dt = dt / 1000.0

        keys = pygame.key.get_pressed()
        dx, dy = 0,0
        if keys[K_LEFT]:
            dx = -PLAYER_SPEED * dt
        if keys[K_RIGHT]:
            dx = PLAYER_SPEED * dt
        if keys[K_UP]:
            dy = -PLAYER_SPEED * dt
        if keys[K_DOWN]:
            dy = PLAYER_SPEED * dt

        self.rect.move_ip(dx, dy)
