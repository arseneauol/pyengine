#! /usr/bin/python3.5
import pygame
import engine
pygame.init()
screen = pygame.display.set_mode((240,180))
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
