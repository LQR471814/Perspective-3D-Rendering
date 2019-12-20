import pygame
from pygame.locals import *
import time
import sys

class camera:
    def __init__(self, rot, coord):
        self.rotation = rot
        self.coord = coord
    def getRotation(self):
        return self.rotation
    def getCoord(self):
        return self.coord
    def setCoord(self, newCoords):
        self.coord = newCoords

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
        self.verts = [[-1, -1, -1], [1, 1, 1], [-1, -1, 1], [1, -1, -1], [-1, 1, -1], [1, -1, 1], [1, 1, -1], [-1, 1, 1], [1, 1, 1]]
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

def transformCoords(coordinates):
    global center
    coordinates[0] += center[0]
    coordinates[1] += center[1]
    return coordinates

Controls = """
[W] = Go forward
[S] = Go backward
[A] = Go left
[D] = Go right
[SPACE] = Go up
[SHIFT] = Go down
"""

pygame.init()
stop = False
center = [200, 200]
blocksize = 100
c1 = camera((0, 0), (0, 0, 2))
b1 = block((0, 0, 0))
screen = pygame.display.set_mode([1280, 720])

screen.fill((0, 0, 0))

def UpdateScr(direction, increment):
    global b1
    global c1

    screen.fill((0, 0, 0))
    print("-----------------------------------------")

    for vert in b1.getVerts():
        finCoords = []
        finCoords.append(int(round((vert[0] / (c1.getCoord()[2] - vert[2]) * blocksize) + (direction * ((c1.getCoord()[0] - b1.getCoord()[0]) / c1.getCoord()[2] - b1.getCoord()[2]) * increment), 1)))
        finCoords.append(int(round((vert[1] / (c1.getCoord()[2] - vert[2]) * blocksize) + (direction * ((c1.getCoord()[1] - b1.getCoord()[1]) / c1.getCoord()[2] - b1.getCoord()[2]) * increment), 1)))
        finCoords = transformCoords(finCoords)
        pygame.draw.circle(screen, (255, 255, 255), finCoords, 3)

    for edge in b1.getEdges():
        coords1 = []
        coords2 = []

        coords1.append(int(round(b1.getVerts()[edge[0]][0] / (c1.getCoord()[2] - b1.getVerts()[edge[0]][2]) * blocksize + (direction * ((c1.getCoord()[0] - b1.getCoord()[0]) / c1.getCoord()[2] - b1.getCoord()[2]) * increment), 1)))
        coords1.append(int(round(b1.getVerts()[edge[0]][1] / (c1.getCoord()[2] - b1.getVerts()[edge[0]][2]) * blocksize + (direction * ((c1.getCoord()[0] - b1.getCoord()[0]) / c1.getCoord()[2] - b1.getCoord()[2]) * increment), 1)))
        coords2.append(int(round(b1.getVerts()[edge[1]][0] / (c1.getCoord()[2] - b1.getVerts()[edge[1]][2]) * blocksize + (direction * ((c1.getCoord()[1] - b1.getCoord()[1]) / c1.getCoord()[2] - b1.getCoord()[2]) * increment), 1)))
        coords2.append(int(round(b1.getVerts()[edge[1]][1] / (c1.getCoord()[2] - b1.getVerts()[edge[1]][2]) * blocksize + (direction * ((c1.getCoord()[1] - b1.getCoord()[1]) / c1.getCoord()[2] - b1.getCoord()[2]) * increment), 1)))

        print((direction * ((c1.getCoord()[0] - b1.getCoord()[0]) / c1.getCoord()[2] - b1.getCoord()[2]) * increment), (direction * ((c1.getCoord()[1] - b1.getCoord()[1]) / c1.getCoord()[2] - b1.getCoord()[2]) * increment))

        coords1 = transformCoords(coords1)
        coords2 = transformCoords(coords2)

        print(coords1, coords2)

        b1.reset()
        #pygame.draw.line(screen, (255, 255, 255), coords1, coords2)

UpdateScr(0, 0)

while stop == False:
    for event in pygame.event.get():
        if event.type == QUIT:
            stop = True
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                stop = True
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_w:
                c1.setCoord([c1.getCoord()[0], c1.getCoord()[1], c1.getCoord()[2] + 0.1])
                UpdateScr(0, 0)
            if event.key == pygame.K_a:
                c1.setCoord([c1.getCoord()[0] - 1, c1.getCoord()[1], c1.getCoord()[2]])
                # center[0] -= 10
                UpdateScr(-1, 10)
            if event.key == pygame.K_d:
                c1.setCoord([c1.getCoord()[0] + 1, c1.getCoord()[1], c1.getCoord()[2]])
                # center[0] += 10
                UpdateScr(1, 10)
            if event.key == pygame.K_s:
                c1.setCoord([c1.getCoord()[0], c1.getCoord()[1], c1.getCoord()[2] - 0.1])
                UpdateScr(0, 0)
            if event.key == pygame.K_SPACE:
                # c1.setCoord([c1.getCoord()[0], c1.getCoord()[1] - 0.1, c1.getCoord()[2]])
                # center[1] -= 10
                UpdateScr(-1, 10)
            if event.key == pygame.K_LSHIFT:
                # c1.setCoord([c1.getCoord()[0], c1.getCoord()[1] + 0.1, c1.getCoord()[2]])
                # center[1] += 10
                UpdateScr(1, 10)

    pygame.display.update()
