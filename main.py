#! /usr/bin/python3.5
import pygame
import engine


def mainUpdate():
    return


def loadScene():
    global Scene
    gameObjects = []
    mtransform =  engine.Transform(engine.Vector2(50, 50),0,0)
    mrendere = engine.Renderer(pygame.image.load("sprite/chat.png"))
    coponents = []
    spaceShip = engine.GameObject(mtransform, mrendere,coponents)
    gameObjects.append(spaceShip)

    scene = engine.Scene(gameObjects)
    return


def loadPreferane():
    return


pygame.init()

screen = pygame.display.set_mode((600, 400))
loadScene()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
