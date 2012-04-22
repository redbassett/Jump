#!/usr/bin/env python

import pygame
from pygame.locals import *
from pygame.sprite import Sprite, Group, spritecollide
"""
A player is a character in the game.  All players are human controlled.
"""

PLAYER_SPEED = 200
JUMP_SPEED = 500
GRAVITY = 700

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
        
        self.inAir = True
     #   self.wallJump = False
        
        self.level = level
        self.bounds = level.bounds
        self.game = game

    def jump(self):
        if not self.inAir:
            self.inAir = True
            self.vy = -JUMP_SPEED

    def update(self, dt):
        dt = dt / 1000.0

        keys = pygame.key.get_pressed()
        self.vx = 0
        if keys[K_LEFT]:
            self.vx = -PLAYER_SPEED
        
        if keys[K_RIGHT]:
            self.vx = PLAYER_SPEED
        
        if keys[K_RIGHT]:
            self.vx = PLAYER_SPEED


        
        dx = self.vx * dt
        dy = self.vy * dt
            
        
        # Again from Alec
        #if self.inAir:
        self.vy += GRAVITY * dt

        prev_rect = self.rect
        self.rect = self.rect.move(dx,dy)
        self.rect.clamp_ip(self.bounds)

        #lethal touches
        # Takes false because lethal blocks need to be there.
        if spritecollide(self, self.level.lethal, False):
            self.game.deaths += 1
            self.game.spawn()
        
        

        #self.inAir = True
        for sprite in spritecollide(self, self.level.blocks, False):
            rect = sprite.rect
                
              # walls
            if self.rect.left < rect.right and prev_rect.left >= rect.right:
                self.rect.left = rect.right
              #  self.wallJump = True
           
            elif self.rect.right >= rect.left and prev_rect.right <= rect.left:
                self.rect.right = rect.left
           #     self.wallJump = True
           # else:
            #    self.wallJump = False

            
                    #ceiling
            if self.rect.top <= rect.bottom and \
                    prev_rect.top >= rect.bottom and \
                    self.rect.colliderect(rect):
                self.vy /= 2.0 #on hitting ceiling, dont need to be stuck and finish arc.
                self.rect.top = rect.bottom
                    
                    #landing
            if self.rect.bottom >= rect.top and \
                    prev_rect.bottom <= rect.top and \
                    self.rect.colliderect(rect):
                self.vy = 0
                self.rect.bottom = rect.top
                self.inAir = False
         
