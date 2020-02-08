# Get pyGame installed on your machine:
# Windows Instructions:
# run 'py -m pip install -U pygame --user' in your command prompt (without the quotes).
# If you get an "Access is denied" error try re-opening your command prompt in administrator mode

# For this project, I want you to modify pong_paddle to return a different color than its default green.
# I've added some helper methods to convert from the game ticks (milliseconds) to a normalized range of
# 0-255.  Make sure to read the comments in pong_paddle, there are some hints there.

import os
import pygame
import pong_paddle

pygame.init()
width, height = (800, 600)
screen = pygame.display.set_mode((width, height))

paddle = [100, 100, 25, 100]

while True:
	paddle_color = pong_paddle.getPongPaddleColorForTime(pygame.time.get_ticks())
	screen.fill(0)
	pygame.draw.rect(screen, paddle_color, paddle)
	pygame.display.flip()

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit() 
			exit(0) 