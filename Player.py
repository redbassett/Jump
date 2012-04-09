#!/usr/bin/env python

import pygame
from pygame.locals import *
from pygame.sprite import Sprite, Group
"""
A player is a character in the game.  All players are human controlled.
"""

PLAYER_SPEED = 240
JUMP_SPEED = 5000

class Player(Sprite):
    def __init__(self, (x,y), level, game, color = (255,255,255), (w,h) = (20,20)):
        Sprite.__init__(self)
        self.x, self.y  = (x,y)
        
        self.image = pygame.Surface((w,h))
        self.rect = self.image.get_rect()
        self.rect.topleft = x,y

        self.image.fill(color)

        self.vx = 0
        self.vy = 0
        
        self.inAir = False
        
        self.level = level
        self.bounds = level.bounds
        self.game = game

    def update(self, dt):
        dt = dt / 1000.0

        keys = pygame.key.get_pressed()
        dx, dy = 0,0
        if keys[K_LEFT]:
            dx = -PLAYER_SPEED * dt
        if keys[K_RIGHT]:
            dx = PLAYER_SPEED * dt
        if keys[K_SPACE] and not self.inAir:
            dy = -JUMP_SPEED * dt
        else:
            dy = PLAYER_SPEED * dt
            
        #self.rect.move_ip(dx, dy)
        
        # Again from Alec
        self.inAir = True

        prev_rect = self.rect
        self.rect = self.rect.move(dx,dy)
        self.rect.clamp_ip(self.bounds)
        
        for sprite in self.touches(self.level.blocks):
            if not sprite.lethal:
                rect = sprite.rect
                
                if self.rect.left <= rect.right and prev_rect.left >= rect.right:
                    self.rect.left = rect.right
                if self.rect.right >= rect.right and prev_rect.right <= rect.left:
                    self.rect.right = rect.left
                if self.rect.top <= rect.bottom and prev_rect.top >= rect.bottom:
                    self.rect.top = rect.bottom
                if self.rect.bottom >= rect.top and prev_rect.bottom <= rect.top:
                    self.dy = 0
                    self.rect.bottom = rect.top
                    self.inAir = False
            else:
                self.game.deaths += 1
                self.game.spawn()
    
    # Using Alec's wonderful collision math
    def touches(self, group):
        touching = Group()
        coll = self.rect.inflate(1,1)
        for sprite in group:
            if coll.colliderect(sprite.rect):
                touching.add(sprite)
        return touching
