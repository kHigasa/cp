import numpy
import matplotlib
import matplotlib.pyplot as plt
import mayavi
import mayavi.mlab

X, Y = numpy.mgrid[-2:2, 0.1, -2:2, 0.1]; Z = X ** 4 + Y ** 4

mayavi.mlab.surf(Z)
mayavi.mlab.axes()
mayavi.mlab.outline()
mlab.show()
