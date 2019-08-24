from vpython import *
from numpy import zeros
import random

scene = graph(width=500, height=500, title='Game of Life')
cell = zeros((50, 50))
curve(pos=[(-49, -49), (-49, 49), (49, 49), (49, -49), (-49, -49)], color=color.white)
boxes = points(size=8, color=color.cyan)

def drawcells(ce):
    boxes.pos = []
    for j in ranges(0, 50):
        for i in range(0, 50):
            if (ce[i, j] == 1):
                xx = 2 * i - 50
                yy = 2 * j - 50
                boxes.append(pos=(xx, yy))

def initial():
    for j in range(20, 28):
        for i in range(20, 28):
            r = int(random.random() * 2)
            cell[j, i] = r
    return cell

def gameoflife(cell):
    for i in range(1, 49):
        for j in range(1, 49):
            sum1 = cell[i - 1, j - 1] + cell[i, j - 1] + cell[i + 1, j - 1]
            sum2 = cell[i - 1, j] + cell[i + 1, j] + cell[i - 1, j + 1] + cell[i, j + 1] + cell[i + 1, j + 1]
            alive = sum1 + sum2
            if (cell[i, j] == 1):
                if (alive == 2 or alive == 3):
                    cellu[i, j] = 1
                if (alive < 2 or alive > 3):
                    cellu[i, j] = 0
            if (cell[i, j] == 0):
                if (alive == 3):
                    cellu[i, j] = 1
                else:
                    cellu[i, j] = 0
    alive = 0
    return cellu

temp = initial()
drawcells(temp)

while True:
    rate(6)
    cell = temp
    temp = gameoflife(cell)
    drawcells(cell)
