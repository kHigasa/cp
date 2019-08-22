from tkinter import *
from numpy import zeros, arange
import math

global Xwidth, Yheight
root = Tk()
root.title('Entropy versus mu')
mumin = 3.5; mumax = 4.0; dmu = 0.005; nbin = 1000; nmax = 100000
prob = zeros((1000), float)
minx = mumin; maxx = mumax; miny = 0; maxy = 2.5; Xwidth = 500; Yheight = 500

c = Canvas(root, width=Xwidth, height=Yheight)
c.pack()

Button(root, text='Quit', command=root.quit).pack()

def world2sc(xl, yt, xr, yb):
    maxx = Xwidth
    maxy = Yheight
    lm = 0.10 * maxx
    rm = 0.90 * maxx
    bm = 0.85 * maxy
    tm = 0.10 * maxy
    mx = (lm - rm) / (xl - xr)
    bx = (xl * rm - xr * lm) / (xl - xr)
    my = (tm - bm) / (yt - yb)
    by = (yb * tm - yt * bm) / (yb - yt)
    linearTr = [mx, bx, my, by]
    return linearTr

def xyaxis(mx, bx, my, by):
    x1 = (int)(mx * minx + bx)
    x2 = (int)(mx * maxx + bx)
    y1 = (int)(my * miny + by)
    y2 = (int)(my * maxy + by)
    yc = (int)(my * 0.0 + by)
    c.create_line(x1, yc, x2, yc, fill='red')
    c.create_line(x1, yc, x1, y2, fill='red')

    for i in range(7):
        x = minx + (i - 1) * 0.1
        x1 = (int)(mx * x + bx)
        x2 = (int)(mx * minx + bx)
        y = miny + i * 0.5
        y2 = (int)(my * y + by)
        c.create_line(x1, yc - 4, x1, yc + 4, fill='red')
        c.create_line(x2 - 4, y2, x2 + 4, y2, fill='red')
        c.create_text(x1 + 10, yc + 10, text='%5.2f'%(x), fill='red', anchor=E)
        c.create_text(x2 + 30, y2, text='%5.2f'%(y), fill='red', anchor=E)
    c.create_text(70, 30, text='entropy', fill='red', anchor=E)
    c.create_text(420, yc - 10, text='mu', fill='red', anchor=E)

mx, bx, my, by = world2sc(minx, maxy, maxx, miny)
xyaxis(mx, bx, my, by)
mu0 = mumin * mx + bx
entr0 = my * 0.0 + by

for mu in arange(mumin, mumax, dmu):
    print(mu)
    for j in range(1, nbin):
        prob[j] = 0
    y = 0.5
    for n in range(1, nmax + 1):
        y = mu * y * (1.0 - y)
        if (n > 30000):
            ibin = int(y * nbin) + 1
            prob[ibin] += 1
    entropy = 0.
    for ibin in range(1, nbin):
        if (prob[ibin] > 0):
            entropy = entropy - (prob[ibin] / nmax) * math.log10(prob[ibin] / nmax)
    entrpc = my * entropy + by
    muc = mx * mu + bx
    c.create_line(mu0, entr0, muc, entrpc, width=1, fill='blue')
    mu0 = muc
    entr0 = entrpc
root.mainloop()
