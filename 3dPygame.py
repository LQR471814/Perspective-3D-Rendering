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

    def rotateX(self, RotationCenter, radians, verticies):
        (cx, cy, cz) = RotationCenter
        for vertex in verticies:
            y = vertex[1] - cy
            z = vertex[2] - cz
            d = math.hypot(y, z)
            theta = math.atan2(y, z) + radians
            vertex[2] = cz + d * math.cos(theta)
            vertex[1] = cy + d * math.sin(theta)
        return verticies

    def rotateY(self, RotationCenter, radians, verticies):
        (cx, cy, cz) = RotationCenter
        for vertex in verticies:
            x = vertex[0] - cx
            z = vertex[2] - cz
            d = math.hypot(x, z)
            theta = math.atan2(x, z) + radians
            vertex[2] = cz + d * math.cos(theta)
            vertex[0] = cx + d * math.sin(theta)
        return verticies

    def rotateZ(self, RotationCenter, radians, verticies):
        (cx, cy, cz) = RotationCenter
        for vertex in verticies:
            x = vertex[0] - cx
            y = vertex[1] - cy
            d = math.hypot(y, x)
            theta = math.atan2(y, x) + radians
            vertex[0] = cx + d * math.cos(theta)
            vertex[1] = cy + d * math.sin(theta)
        return verticies

class block:
    def __init__(self, coordinate):
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
    def getVerts(self):
        return self.verts

    def getEdges(self):
        return self.edges

    def getCoord(self):
        return self.coord

    def setCoord(self, newCoords):
        self.coord = newCoords

    def rotateX(self, RotationCenter, radians, verticies):
        (cx, cy, cz) = RotationCenter
        for vertex in verticies:
            y = vertex[1] - cy
            z = vertex[2] - cz
            d = math.hypot(y, z)
            theta = math.atan2(y, z) + radians
            vertex[2] = cz + d * math.cos(theta)
            vertex[1] = cy + d * math.sin(theta)
        return verticies

    def rotateY(self, RotationCenter, radians, verticies):
        (cx, cy, cz) = RotationCenter
        for vertex in verticies:
            x = vertex[0] - cx
            z = vertex[2] - cz
            d = math.hypot(x, z)
            theta = math.atan2(x, z) + radians
            vertex[2] = cz + d * math.cos(theta)
            vertex[0] = cx + d * math.sin(theta)
        return verticies

    def rotateZ(self, RotationCenter, radians, verticies):
        (cx, cy, cz) = RotationCenter
        print(verticies)
        print(cx, cy, cz)
        for vertex in verticies:
            x = vertex[0] - cx
            y = vertex[1] - cy
            d = math.hypot(y, x)
            theta = math.atan2(y, x) + radians
            vertex[0] = cx + d * math.cos(theta)
            vertex[1] = cy + d * math.sin(theta)
        return verticies

def transformCoords(coordinates):
    global center
    coordinates[0] += center[0]
    coordinates[1] += center[1]
    return coordinates

def UpdateScr(increment):
    global b1
    global c1

    screen.fill((0, 0, 0))
    print("-----------------------------------------")

    for vert in b1.getVerts():
        finCoords = []
        finCoords.append(int(round((vert[0] / (c1.getCoord()[2] - vert[2]) * blocksize) + ((c1.getCoord()[0] - vert[0]) / (c1.getCoord()[2] - vert[2]) * increment), 1)))
        finCoords.append(int(round((vert[1] / (c1.getCoord()[2] - vert[2]) * blocksize) + ((c1.getCoord()[1] - vert[1]) / (c1.getCoord()[2] - vert[2]) * increment), 1)))
        finCoords = transformCoords(finCoords)
        pygame.draw.circle(screen, (255, 255, 255), finCoords, 3)

    for edge in b1.getEdges():
        coords1 = []
        coords2 = []

        coords1.append(int(round((b1.getVerts()[edge[0]][0] / (c1.getCoord()[2] - b1.getVerts()[edge[0]][2])) * blocksize + ((c1.getCoord()[0] - b1.getVerts()[edge[0]][0]) / (c1.getCoord()[2] - b1.getVerts()[edge[0]][2]) * increment), 1)))
        coords1.append(int(round((b1.getVerts()[edge[0]][1] / (c1.getCoord()[2] - b1.getVerts()[edge[0]][2])) * blocksize + ((c1.getCoord()[1] - b1.getVerts()[edge[0]][1]) / (c1.getCoord()[2] - b1.getVerts()[edge[0]][2]) * increment), 1)))

        coords2.append(int(round((b1.getVerts()[edge[1]][0] / (c1.getCoord()[2] - b1.getVerts()[edge[1]][2])) * blocksize + ((c1.getCoord()[0] - b1.getVerts()[edge[1]][0]) / (c1.getCoord()[2] - b1.getVerts()[edge[1]][2]) * increment), 1)))
        coords2.append(int(round((b1.getVerts()[edge[1]][1] / (c1.getCoord()[2] - b1.getVerts()[edge[1]][2])) * blocksize + ((c1.getCoord()[1] - b1.getVerts()[edge[1]][1]) / (c1.getCoord()[2] - b1.getVerts()[edge[1]][2]) * increment), 1)))
        coords1 = transformCoords(coords1)
        coords2 = transformCoords(coords2)

        print(coords1, coords2)

        b1.reset()
        pygame.draw.line(screen, (255, 255, 255), coords1, coords2)

Controls = """
[W] = Go forward
[S] = Go backward
[A] = Go left
[D] = Go right
[SPACE] = Go up
[SHIFT] = Go down
[LEFT] = Rotate Left
[RIGHT] = Rotate Right
"""

print(Controls)
pygame.init()
stop = False
center = [200, 200]
blocksize = 100
c1 = camera((0, 0), (0, 0, 2), 3, 0.05)
b1 = block((0, 0, 0))
screen = pygame.display.set_mode([1280, 720])

screen.fill((0, 0, 0))

UpdateScr(c1.getSpeedStrafe())
pygame.display.update()

while stop == False:
    keystate = pygame.key.get_pressed()

    if keystate[pygame.K_ESCAPE]:
        stop = True
        pygame.quit()
        sys.exit()

    if keystate[pygame.K_LEFT]:
        b1.setCoord([b1.rotateZ(RotationCenter=b1.getCoord(), radians=c1.getRotation()[0] - 0.1, verticies=b1.getVerts()), b1.getCoord()[1], b1.getCoord()[2]])

    if keystate[pygame.K_LEFT]:
        b1.setCoord([b1.rotateZ(RotationCenter=b1.getCoord(), radians=c1.getRotation()[0] + 0.1, verticies=b1.getVerts()), b1.getCoord()[1], b1.getCoord()[2]])

    if keystate[pygame.K_w]:
        c1.setCoord([c1.getCoord()[0], c1.getCoord()[1], c1.getCoord()[2] - c1.getSpeedStraight()])
        UpdateScr(c1.getSpeedStrafe())

    if keystate[pygame.K_a]:
        c1.setCoord([c1.getCoord()[0] - 1, c1.getCoord()[1], c1.getCoord()[2]])
        UpdateScr(c1.getSpeedStrafe())

    if keystate[pygame.K_d]:
        c1.setCoord([c1.getCoord()[0] + 1, c1.getCoord()[1], c1.getCoord()[2]])
        UpdateScr(c1.getSpeedStrafe())

    if keystate[pygame.K_s]:
        c1.setCoord([c1.getCoord()[0], c1.getCoord()[1], c1.getCoord()[2] + c1.getSpeedStraight()])
        UpdateScr(c1.getSpeedStrafe())

    if keystate[pygame.K_SPACE]:
        c1.setCoord([c1.getCoord()[0], c1.getCoord()[1] - 1, c1.getCoord()[2]])
        UpdateScr(c1.getSpeedStrafe())

    if keystate[pygame.K_LSHIFT]:
        c1.setCoord([c1.getCoord()[0], c1.getCoord()[1] + 1, c1.getCoord()[2]])
        UpdateScr(c1.getSpeedStrafe())

    for event in pygame.event.get():
        if event.type == QUIT:
            stop = True
            pygame.quit()
            sys.exit()

    pygame.display.update()

