import matplotlib.pylab as p
import numpy
from mpl_toolkits.mplot3d import Axes3D
from numpy import *;

Nmax = 100; Niter = 50
V = zeros((Nmax, Nmax), float)
print ("Working hard, wait for the figure while I count to 60")

for k in range(0, Nmax-1):
    V[0,k] = 100.0
for iter in range(Niter):
    if iter%10 == 0: print(iter)
    for i in range(1, Nmax-2):
        for j in range(1,Nmax-2):
            V[i,j] = 0.25*(V[i+1,j]+V[i-1,j]+V[i,j+1]+V[i,j-1])
    print ("iter, V[Nmax/5,Nmax/5]", iter, V[Nmax/5,Nmax/5])
x = range(0, 50, 2); y = range(0, 50, 2)
X, Y = p.meshgrid(x,y)

def functz(V):
    z = V[X,Y]
    return z

Z = functz(V)
fig = p.figure()
ax = Axes3D(fig)
ax.plot_wireframe(X, Y, Z, color = 'r')
ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('V(x,y)')
ax.set_title('Potential within Square V(x=0)=100V (Rotatable)')
p.show()
