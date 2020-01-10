import pygame
from pygame.locals import *
import time
import sys
import math

class camera:
    def __init__(self, rot, coord, strafeSpeed, straightSpeed):
        self.rotation = rot
        self.coord = coord
        self.speedStrafe = strafeSpeed
        self.speedStraight = straightSpeed
    def getRotation(self):
        return self.rotation
    def getCoord(self):
        return self.coord
    def getSpeedStraight(self):
        return self.speedStraight
    def getSpeedStrafe(self):
        return self.speedStrafe
    def setCoord(self, newCoords):
        self.coord = newCoords

class block:
    def __init__(self, coordinate, rotation):
        self.rotationIncrement = 0.01
        self.rotationIncrementTheta = 0
        self.rotationIncrementPhi = 0
        self.verts = [[-1, -1, -1], [1, 1, 1], [-1, -1, 1], [1, -1, -1], [-1, 1, -1], [1, -1, 1], [1, 1, -1], [-1, 1, 1]]
        self.edges = [[4, 0],
                      [4, 6],
                      [4, 7],
                      [7, 2],
                      [7, 1],
                      [6, 3],
                      [6, 1],
                      [0, 3],
                      [0, 2],
                      [3, 6],
                      [3, 5],
                      [2, 5],
                      [5, 1]
                      ]
        self.coord = coordinate
        self.rotation = rotation

    def reset(self):
        self.verts = [[-1, -1, -1], [1, 1, 1], [-1, -1, 1], [1, -1, -1], [-1, 1, -1], [1, -1, 1], [1, 1, -1], [-1, 1, 1]]
        self.edges = [[4, 0],
                      [4, 6],
                      [4, 7],
                      [7, 2],
                      [7, 1],
                      [6, 3],
                      [6, 1],
                      [0, 3],
                      [0, 2],
                      [3, 6],
                      [3, 5],
                      [2, 5],
                      [5, 1]
                      ]
    def getRotation(self):
        return self.rotation
    def setRotation(self, rotation):
        self.rotation = rotation
    def getVerts(self):
        return self.verts
    def getEdges(self):
        return self.edges
    def getCoord(self):
        return self.coord
    def setCoord(self, newCoords):
        self.coord = newCoords

def transformCoords(coordinates):
    global center
    coordinates[0] += center[0]
    coordinates[1] += center[1]
    return coordinates

def UpdateScr(increment, block):
    global b1
    global c1

    screen.fill((0, 0, 0))
    # print("-----------------------------------------")

    for vert in b1.getVerts():
        finCoords = []
        vert = Rotate3D(vert, block)
        finCoords.append(int(round((vert[0] / (c1.getCoord()[2] - vert[2]) * blocksize) + ((c1.getCoord()[0] - vert[0]) / (c1.getCoord()[2] - vert[2]) * increment), 1)))
        finCoords.append(int(round((vert[1] / (c1.getCoord()[2] - vert[2]) * blocksize) + ((c1.getCoord()[1] - vert[1]) / (c1.getCoord()[2] - vert[2]) * increment), 1)))
        finCoords = transformCoords(finCoords)
        # print(Rotate3D(vert, block))
        pygame.draw.circle(screen, (255, 255, 255), RotateCoords(finCoords, block), 3)
        # pygame.draw.circle(screen, (255, 255, 255), finCoords, 3)

    for edge in b1.getEdges():
        coords1 = []
        coords2 = []

        coords1.append(int(round((b1.getVerts()[edge[0]][0] / (c1.getCoord()[2] - b1.getVerts()[edge[0]][2])) * blocksize + ((c1.getCoord()[0] - b1.getVerts()[edge[0]][0]) / (c1.getCoord()[2] - b1.getVerts()[edge[0]][2]) * increment), 1)))
        coords1.append(int(round((b1.getVerts()[edge[0]][1] / (c1.getCoord()[2] - b1.getVerts()[edge[0]][2])) * blocksize + ((c1.getCoord()[1] - b1.getVerts()[edge[0]][1]) / (c1.getCoord()[2] - b1.getVerts()[edge[0]][2]) * increment), 1)))

        coords2.append(int(round((b1.getVerts()[edge[1]][0] / (c1.getCoord()[2] - b1.getVerts()[edge[1]][2])) * blocksize + ((c1.getCoord()[0] - b1.getVerts()[edge[1]][0]) / (c1.getCoord()[2] - b1.getVerts()[edge[1]][2]) * increment), 1)))
        coords2.append(int(round((b1.getVerts()[edge[1]][1] / (c1.getCoord()[2] - b1.getVerts()[edge[1]][2])) * blocksize + ((c1.getCoord()[1] - b1.getVerts()[edge[1]][1]) / (c1.getCoord()[2] - b1.getVerts()[edge[1]][2]) * increment), 1)))
        coords1 = transformCoords(coords1)
        coords2 = transformCoords(coords2)

        b1.reset()
        # pygame.draw.line(screen, (255, 255, 255), coords1, coords2)
    time.sleep(0.005)

def RotateCoords(coordinates, block):
    polarCoords = [0, 0]
    returnCoords = [0, 0]
    polarCoords[0] = math.sqrt(coordinates[0] ** 2 + coordinates[1] ** 2)
    polarCoords[1] = math.atan2(coordinates[1], coordinates[0])

    polarCoords[1] = polarCoords[1] + block.getRotation()

    returnCoords[0] = int(round(polarCoords[0] * math.cos(polarCoords[1]), 0))
    returnCoords[1] = int(round(polarCoords[0] * math.sin(polarCoords[1]), 0))

    return returnCoords

def Rotate3D(coordinates, block):
    sphericalCoordinates = [0, 0, 0]
    returnCoordinates = coordinates

    sphericalCoordinates[0] = math.sqrt(returnCoordinates[0] ** 2 + returnCoordinates[1] ** 2 + returnCoordinates[2] ** 2)
    sphericalCoordinates[1] = math.atan2(returnCoordinates[1], returnCoordinates[0])
    sphericalCoordinates[2] = math.acos(returnCoordinates[2] / ( math.sqrt(returnCoordinates[0] ** 2 + returnCoordinates[1] ** 2 + returnCoordinates[2] ** 2)))

    sphericalCoordinates[1] += block.rotationIncrementTheta
    sphericalCoordinates[2] += block.rotationIncrementPhi

    returnCoordinates[0] = sphericalCoordinates[0] * math.sin(sphericalCoordinates[2]) * math.cos(sphericalCoordinates[1])
    returnCoordinates[1] = sphericalCoordinates[0] * math.sin(sphericalCoordinates[2]) * math.sin(sphericalCoordinates[1])
    returnCoordinates[2] = sphericalCoordinates[0] * math.cos(sphericalCoordinates[2])

    return returnCoordinates

Controls = """
[W] = Go forward
[S] = Go backward
[A] = Go left
[D] = Go right
[SPACE] = Go up
[SHIFT] = Go down
[Q] = Rotate counter clockwise around (0, 0)
[E] = Rotate clockwise around (0, 0)
[LEFT] = Rotate counter clockwise around center of object
[RIGHT] = Rotate clockwise around center of object
[UP] = Some weird ping pong thing
[DOWN] = Some weird ping pong thing
"""

print(Controls)
pygame.init()
stop = False
center = [300, 300]
blocksize = 100
c1 = camera((0, 0), (0, 0, 2), 3, 0.05)
b1 = block((0, 0, 0), 0)
screen = pygame.display.set_mode([1280, 720])

screen.fill((0, 0, 0))

UpdateScr(c1.getSpeedStrafe(), b1)
pygame.display.update()

while stop == False:
    keystate = pygame.key.get_pressed()

    if keystate[pygame.K_ESCAPE]:
        stop = True
        pygame.quit()
        sys.exit()

    if keystate[pygame.K_w]:
        c1.setCoord([c1.getCoord()[0], c1.getCoord()[1], c1.getCoord()[2] - c1.getSpeedStraight()])
        UpdateScr(c1.getSpeedStrafe(), b1)

    if keystate[pygame.K_a]:
        c1.setCoord([c1.getCoord()[0] - 1, c1.getCoord()[1], c1.getCoord()[2]])
        UpdateScr(c1.getSpeedStrafe(), b1)

    if keystate[pygame.K_d]:
        c1.setCoord([c1.getCoord()[0] + 1, c1.getCoord()[1], c1.getCoord()[2]])
        UpdateScr(c1.getSpeedStrafe(), b1)

    if keystate[pygame.K_s]:
        c1.setCoord([c1.getCoord()[0], c1.getCoord()[1], c1.getCoord()[2] + c1.getSpeedStraight()])
        UpdateScr(c1.getSpeedStrafe(), b1)

    if keystate[pygame.K_SPACE]:
        c1.setCoord([c1.getCoord()[0], c1.getCoord()[1] - 1, c1.getCoord()[2]])
        UpdateScr(c1.getSpeedStrafe(), b1)

    if keystate[pygame.K_LSHIFT]:
        c1.setCoord([c1.getCoord()[0], c1.getCoord()[1] + 1, c1.getCoord()[2]])
        UpdateScr(c1.getSpeedStrafe(), b1)

    if keystate[pygame.K_q]:
        b1.setRotation(b1.getRotation() + b1.rotationIncrement * 1)
        UpdateScr(c1.getSpeedStrafe(), b1)

    if keystate[pygame.K_e]:
        b1.setRotation(b1.getRotation() + b1.rotationIncrement * -1)
        UpdateScr(c1.getSpeedStrafe(), b1)

    if keystate[pygame.K_RIGHT]:
        b1.rotationIncrementTheta += 0.05
        UpdateScr(c1.getSpeedStrafe(), b1)

    if keystate[pygame.K_LEFT]:
        b1.rotationIncrementTheta += -0.05
        UpdateScr(c1.getSpeedStrafe(), b1)

    if keystate[pygame.K_UP]:
        b1.rotationIncrementPhi += 0.05
        UpdateScr(c1.getSpeedStrafe(), b1)

    if keystate[pygame.K_DOWN]:
        b1.rotationIncrementPhi += -0.05
        UpdateScr(c1.getSpeedStrafe(), b1)

    for event in pygame.event.get():
        if event.type == QUIT:
            stop = True
            pygame.quit()
            sys.exit()

    pygame.display.update()