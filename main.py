#!/usr/bin/env python

from Game import *

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Jump')

game = Game(screen)
try:
    game.loop()
except KeyboardInterrupt:
    game.quit()
