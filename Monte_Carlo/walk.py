from vpython import *
import random

random.seed(None)
jmax = 20
x = 0.; y = 0.

graph1 = graph(width = 500, height = 500, title = 'Random walk', xtitle = 'x', ytitle = 'y')

pts = gcurve(color = color.yellow)

for i in range(0, jmax + 1):
    pts.plot(pos = (x, y))
    x += (random.random() - 0.5) * 2
    y += (random.random() - 0.5) * 2
    pts.plot(pos = (x, y))
    rate(100)
