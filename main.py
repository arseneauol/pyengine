#! /usr/bin/python3.5
import pygame
import engine
pygame.init()

screen = pygame.display.set_mode((600,400))
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
def loadScene():
  global Scene
  gameObjects = []

  mtransform = engine.Transform(engine.Vector2(50,50))
  spaceShip = engine.GameObject(mtransform,engine.Renderer())

  gameObjects.append(spaceShip)



  scene =  engine.Scene(gameObjects)
  return
def loadPreferane():
  return