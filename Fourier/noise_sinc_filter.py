from vpython import *
import numpy as np
import random
import math

max = 4000
array = np.zeros((max), float)
ps = np.zeros((max), float)
step = 2 * math.pi / 1000
graph1 = graph(x=0, y=0, width=600, height=250, title='Pure Signal', xtitle='t (s)', ytitle='f(t)', xmin=0, xmax=25, ymin=0, ymax=10)
funct1 = gcurve(color=color.red)
graph2 = graph(x=0, y=250, width=600, height=250, title='Signal + Noise', xtitle='t (s)', ytitle='y(t)', xmin=0, xmax=25, ymin=0, ymax=10)
funct2 = gcurve(color=color.red)
graph3 = graph(x=0, y=500, width=600, height=250, title='Filtered Input', xtitle='t (s)', ytitle='y(t)', xmin=0, xmax=25, ymin=0, ymax=10)
funct3 = gcurve(color=color.red)

def function(array, max):
    f = np.zeros((max + 1), float)
    step = 2  * pi / 1000; x = 0.
    for i in range(0, max):
        f[i] = 1 / (1. - 0.9 * sin(x)
        array[i] = (1 / (1 - 0.9 * sin(x))) + 0.5 * (2. * random.random() - 1)
        funct1.plot(pos = (x, f[i]))
        funct2.plot(pos = (x, array[i]))
        x += step

def filter():
    y = np.zeros((max), float); h = np.zeros((max), float)
    step = 2 * pi / 1000
    m = 100
    fc = .07
    for i in range(0, 100):
        if ((i - (m / 2)) == 0):
            h[i] = 2 * pi * fc
        if ((i - (m / 2)) != 0):
            h[i] = sin(2 * pi * fc * (i - m / 2)) / (i - m / 2)
        h[i] = h[i] * (0.54 - 0.46 * cos(2 * pi * i / m))
    sum = 0.
    for i in range(0, 100):
        sum = sum + h[i]
    for i in range(0, 100):
        h[i] = h[i] / sum
    for j in range(100, max - 1):
        y[j] = 0.
        for i in range(0, 100):
            y[j] = y[j] + array[j - i] * h[i]
    for j in range(0, max - 1):
        funct3.plot(pos = (j * step, y[j]))

function(array, max)
filter()
