from vpython import *
import numpy as np

a = 0.
b = 10.
n = 100
ydumb = np.zeros((2), float)
y = np.zeros((2), float)
fReturn = np.zeros((2), float)
k1 = np.zeros((2), float)
k2 = np.zeros((2), float)
k3 = np.zeros((2), float)
k4 = np.zeros((2), float)
y[0] = 3.
y[1] = -5.
t = a
h = (b - a) / n

def f(t, y):
    fReturn[0] = y[1]
    fReturn[1] = -100. * y[0] - 2. * y[1] + 10. * sin(3. * t)
    return fReturn

graph1 = graph(x = 0, y = 0, width = 400, height = 400, title = 'RK4', xtitle = 't', ytitle = 'Y[0]', xmin = 0, xmax = 10, ymin = -2, ymax = 3)
funct1 = gcurve(color = color.yellow)
graph2 = graph(x = 400, y = 0, width = 400, height = 400, title = 'RK4', xtitle = 't', ytitle = 'Y[1]', xmin = 0, xmax = 10, ymin = -25, ymax = 18)
funct2 = gcurve(color = color.red)

def rk4(t, h, n):
    k1 = [0] * (n)
    k2 = [0] * (n)
    k3 = [0] * (n)
    k4 = [0] * (n)
    fR = [0] * (n)
    ydumb = [0] * (n)
    fR = f(t, y)
    for i in range(0, n):
        k1[i] = h * fR[i]
    for i in range(0, n):
        ydumb[i] = y[i] + k1[i] / 2.
    k2 = h * f(t + h / 2., ydumb)
    for i in range(0, n):
        ydumb[i] = y[i] + k2[i] / 2.
    k3 = h * f(t + h / 2., ydumb)
    for i in range(0, n):
        ydumb[i] = y[i] + k3[i]
    k4 = h * f(t + h, ydumb)
    for i in range(0, 2):
        y[i] = y[i] + (k1[i] + 2. * (k2[i] + k3[i]) + k4[i]) / 6.
    return y

while (t < b):
    if ((t + h) > b):
        h = b - t
    y = rk4(t, h, 2)
    t = t + h
    rate(30)
    funct1.plot(pos = (t, y[0]))
    funct2.plot(pos = (t, y[1]))
