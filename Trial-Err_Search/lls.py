import pylab as p 
from numpy import *
from numpy.linalg import inv, solve 

nd = 7
A = zeros((3, 3), float); bvec = zeros((3,1), float)
ss = sx = sxx = sy = sxxx = sxxxx = sxy = sxy = sxxy = 0.
x = array([1., 1.1, 1.24, 1.35,  1.451, 1.5, 1.92])
y = array([0.52, 0.8, 0.7, 1.8, 2.9, 2.9, 3.6])
sig = array([0.1, 0.1, 0.2, 0.3, 0.2, 0.1, 0.1])
xRange = arange(1.0, 2.0, 0.1)
p.plot(x, y, 'bo')
p.errorbar(x, y, sig)
p.title('Least Square Fit of Parabola to Blue Data')
p.xlabel('x'); p.ylabel('y'); p.grid(True)

for i in range(0, nd):
        sig2 = sig[i] * sig[i]
        ss  += 1. / sig2; sx += x[i] / sig2; sy += y[i] / sig2
        rhl  = x[i] * x[i]; sxx += rhl / sig2; sxxy += rhl * y[i] / sig2
        sxy += x[i] * y[i] / sig2; sxxx += rhl * x[i] / sig2; sxxxx += rhl * rhl / sig2
A    = array([[ss, sx, sxx], [sx, sxx, sxxx], [sxx, sxxx, sxxxx]])
bvec = array([sy, sxy, sxxy])
xvec = multiply(inv(A), bvec)
print('\n x via Inverse A\n', xvec, '\n' )
xvec = solve(A, bvec)
print('\n x via Elimination \n', xvec, '\n Fit to Parabola\n')
print('y(x) = a0 + a1 x + a2 x^2\n a0 =', x[0],'a1 =', x[1], 'a2 =', x[2])
print('\n i   xi     yi    yfit   ')
for i in range(0, nd):
    s = xvec[0] + xvec[1] * x[i] + xvec[2] * x[i] * x[i]
    print(" %d %5.3f  %5.3f  %8.7f" %(i, x[i], y[i], s))

curve  = xvec[0] + xvec[1] * xRange + xvec[2] * xRange ** 2
points = xvec[0] + xvec[1] * x + xvec[2] * x ** 2
p.plot(xRange, curve,'r', x, points, 'ro')
p.show()
