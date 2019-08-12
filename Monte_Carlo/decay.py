from vpython import *
import random

lambda1 = 0.01
max = 50.; time_max = 500; seed = 68111
number = nloop = max
#random.seed(seed)

graph1 = graph(width = 500, height = 500, title = 'Spontaneous Decay', xtitle = 'Time', ytitle = 'Number left', xmax = 500, xmin = 0, ymax = 100, ymin = 0)
decayfunc = gcurve(color = color.green)

for time in arange(0, time_max + 1):
    for atom in arange(1, number + 1):
        decay = random.random()
        if (decay < lambda1):
            nloop = nloop - 1
    number = nloop
    decayfunc.plot(pos = (time, number))
    rate(30)
