from vpython import *
import numpy as np

a = 0.; b = 10.
Tol = 1.0E-8
ydumb = np.zeros((2), float)
y = np.zeros((2), float)
fReturn = np.zeros((2), float)
err = np.zeros((2), float)
k1 = np.zeros((2), float)
k2 = np.zeros((2), float)
k3 = np.zeros((2), float)
k4 = np.zeros((2), float)
k5 = np.zeros((2), float)
k6 = np.zeros((2), float)
n = 20
y[0] = 1.; y[1] = 0.

h = (b - a) / n; t = a; j = 0
hmin = h / 64; hmax = h * 64
flops = 0; Eexact = 0.; error = 0.
sum = 0.

def f(t, y, fReturn):
    fReturn[0] = y[1]
    fReturn[1] = -6. * pow(y[0], 5.)

graph1 = graph(width = 600, height = 600, title = 'RK 45', xtitle = 't', ytitle = 'Y[0]')
funct1 = gcurve(color = color.blue)
graph2 = graph(width = 500, height = 500, title = 'RK45', xtitle = 't', ytitle = 'Y[1]')
funct2 = gcurve(color = color.red)
funct1.plot(pos = (t, y[0]))
funct2.plot(pos = (t, y[1]))

while (t < b):
    funct1.plot(pos = (t, y[0]))
    funct2.plot(pos = (t, y[1]))
    if ((t + h) > b):
        h = b - t
    f(t, y, fReturn)
    k1[0] = h * fReturn[0]; k1[1] = h * fReturn[1]
    for i in range(0, 2):
        ydumb[i] = y[i] + k1[i] / 4
    f(t + h / 4, ydumb, fReturn)
    k2[0] = h * fReturn[0]; k2[1] = h * fReturn[1]
    for i in range(0, 2):
        ydumb[i] = y[i] + 3 * k1[i] / 32 + 9 * k2[i] / 32
    f(t + 3 * h / 8, ydumb, fReturn)
    k3[0] = h * fReturn[0]; k3[1] = h * fReturn[1]
    for i in range(0, 2):
        ydumb[i] = y[i] + 1932 *k1[i] / 2197 - 7200 * k2[i] / 2197. + 7296 * k3[i] / 2197
    f(t + 12 * h / 13, ydumb, fReturn)
    k4[0] = h * fReturn[0]; k4[1] = h * fReturn[1]
    for i in range(0, 2):
        ydumb[i] = y[i] + 439 * k1[i] / 216 - 8 * k2[i] + 3680 * k3[i] / 513 - 845 * k4[i] / 4104
    f(t + h, ydumb, fReturn)
    k5[0] = h * fReturn[0]; k5[1] = h * fReturn[1]
    for i in range(0, 2):
        ydumb[i] = y[i] - 8 * k1[i] / 27 + 2 * k2[i] - 3544 * k3[i] / 2565 + 1859 * k4[i] / 4104 - 11 * k5[i] / 40
    f(t + h / 2, ydumb, fReturn)
    k6[0] = h * fReturn[0]; k6[1] = h * fReturn[1]
    for i in range(0, 2):
        err[i] = abs(k1[i] / 360 - 128 * k3[i] / 4275 - 2197 * k4[i] / 75240 + k5[i] / 50. + 2 * k6[i] / 55)
    if (err[0] < Tol or err[1] < Tol or h <= 2 * hmin):
        for i in range(0, 2):
            y[i] = y[i] + 25 * k1[i] / 216. + 1408 * k3[i] / 2565. + 2197 * k4[i] / 4104. - k5[i] / 5.
        t = t + h
        j = j + 1
    if (err[0] == 0 or err[1] == 0):
        s = 0
    else:
        s = 0.84 * pow(Tol * h / err[0], 0.25)
    if (s < 0.75 and h > 2 * hmin):
        h /= 2.
    else:
        if (s > 1.5 and 2 * h < hmax):
            h *= 2.
    flops = flops + 1
    E = pow(y[0], 6.) + 0.5 * y[1] * y[1]
    Eexact = 1.
    error = abs((E - Eexact) / Eexact)
    sum +=  error
print(" <error>=  ", sum/flops, ", flops = ", flops)
