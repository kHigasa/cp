from vpython import *
import cmath

N = 100; twopi = 2. * pi; h = twopi / N;  sq2pi = 1. / sqrt(twopi)
y = zeros(N + 1, float); ycomplex = zeros(N, complex)

SignalGraph = graph(x=0, y=0, width=600, height=250, title ='Signal y(t)', xtitle='x', ytitle='y(t)', xmax=2.*math.pi, xmin=0, ymax=30, ymin=-30)
SignalCurve = gcurve(color=color.yellow, display=SignalGraph)
TransformGraph = graph(x=0, y=250, width=600, height=250, title = 'Im Y(omega)', xtitle = 'x', ytitle='Im Y(omega)', xmax=10., xmin=-1, ymax=100, ymin=-250)
TransformCurve = gvbars(delta = 0.05, color = color.red, display = TransformGraph)

def Signal(y):
    h = twopi / N; x = 0.
    for i in range(0, N + 1):
        y[i] = 30 * cos(x) + 60 * sin(2 * x) + 120 * sin(3 * x)
        SignalCurve.plot(pos = (x, y[i]))
        x += h

def DFT(ycomplex):
    for n in range(0, N):
        zsum = complex(0.0, 0.0)
        for k in range(0, N):
            zexpo = complex(0, twopi * k * n / N)
            zsum += y[k] * exp(-zexpo)
        ycomplex[n] = zsum * sq2pi
        if (ycomplex[n].imag != 0): 
            TransformCurve.plot(pos = (n, ycomplex[n].imag)) 

Signal(y)
DFT(ycomplex)
