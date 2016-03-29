import pygame
import sys

from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Drawing time')

BLACK = (  0,   0,   0) # R G B
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

DISPLAYSURF.fill(WHITE) 
pygame.draw.rect(DISPLAYSURF, RED, (0, 0, 100, 100))
#draw 100x100 BLUE rectangle in the top right corner
pygame.draw.rect(DISPLAYSURF, GREEN, (300, 200, 400, 300))
pygame.draw.line(DISPLAYSURF, BLUE, (0, 0), (400, 300), 4)
pygame.draw.circle(DISPLAYSURF, BLACK, (200, 150), 50, 0)
pygame.draw.polygon(DISPLAYSURF, GREEN, ((10,10), (100, 10), (150, 30), (200, 50), (20, 200)))
pygame.draw.ellipse(DISPLAYSURF, RED, (10, 10, 50, 30))

while True: # main game loop
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()