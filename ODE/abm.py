from vpython import *

numgr = graph(x=0, y=0, width=600, height=300, xmin=0.0, xmax = 3.0, title="Numerical Solution", xtitle='t', ytitle='y', ymax=2., ymin=0.9)
numsol = gcurve(color = color.yellow)
exactgr = graph(x=0, y=300, width=600, height=300, title="Exact solution", xtitle='t', ytitle='y', xmax=3.0, xmin=0.0, ymax=2.0, ymin=0.9)
exsol = gcurve(color = color.cyan)
n = 24
A = 0; B = 3.
t = [0] * 500; y = [0] * 500; yy=[0] * 4

def f(t, y):
    return (t - y) / 2.0

def rk4(t, yy, h1):
    for i in range(0, 3):
        t  = h1 * i
        k0 = h1 * f(t, y[i])
        k1 = h1 * f(t + h1 / 2., yy[i] + k0 / 2.)
        k2 = h1 * f(t + h1 / 2., yy[i] + k1 / 2.)
        k3 = h1 * f(t + h1, yy[i] + k2)
        yy[i + 1] = yy[i] + (1. / 6.) * (k0 + 2. * k1 + 2. * k2 + k3)
        print(i, yy[i])
    return yy[3]

def ABM(a, b, N):
   h = (b - a) / N
   t[0] = a; y[0] = 1.00; F0 = f(t[0], y[0])
   for k in range(1, 4):
       t[k] = a + k * h
   y[1] = rk4(t[1], y, h)
   y[2] = rk4(t[2], y, h)
   y[3] = rk4(t[3], y, h)
   F1 = f(t[1], y[1])
   F2 = f(t[2], y[2])
   F3 = f(t[3], y[3])
   h2 = h / 24.

   for k in range(3, N):
       p = y[k] + h2 * (-9. * F0 + 37. * F1 - 59. * F2 + 55. * F3)
       t[k + 1] = a + h * (k + 1)
       F4 = f(t[k + 1], p)
       y[k + 1] = y[k] + h2 * (F1 - 5. * F2 + 19. * F3 + 9. * F4)
       F0 = F1
       F1 = F2
       F2 = F3
       F3 = f(t[k + 1], y[k + 1])
   return t, y

print("  k     t      Y numerical      Y exact")
t, y = ABM(A, B, n)
for k in range(0, n + 1):
    print (" %3d  %5.3f  %12.11f  %12.11f " % (k, t[k], y[k], (3. * exp(-t[k] / 2.) - 2. + t[k])))
    numsol.plot(pos = (t[k], y[k]))
    exsol.plot(pos = (t[k], 3. * exp(-t[k] / 2.) - 2. + t[k]))
