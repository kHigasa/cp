from numpy import *
from numpy.linalg import eig

I = array([[2./3, -1./4, -1./4], [-1./4, 2./3, -1./4], [-1./4, -1./4, 2./3]])
print('\n I = \n', I)

Evals, Evecs = eig(I)
print('\n Eigenvalues = \n', Evals)
print('\n Matrix of Eigenvectors =\n', Evecs)


Vec = array([Evecs[0, 0], Evecs[0, 1], Evecs[0, 2]])
print('\n A single eigenvector to test RHS vs LHS =', Vec, '\n')

LHS = dot(I, Vec)
RHS = dot(Vec, Evals[0])
print('LHS - RHS =\n', LHS-RHS)
