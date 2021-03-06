#!/usr/bin/env python



import numpy as np
import matplotlib.cbook
import matplotlib.mlab as mlab
import warnings
warnings.filterwarnings("ignore", category=matplotlib.cbook.MatplotlibDeprecationWarning)


# the x and y dimensions of our cladera 
dim_x = 100
dim_y = 100


delta = 10
x = np.arange(0, dim_x+1, delta)
y = np.arange(0, dim_y+1, delta)
X, Y = np.meshgrid(x, y)

def caldera_sim_function(x, y):
    x, y = x / 10.0, y / 10.0
    z0 = mlab.bivariate_normal(x, y, 10.0, 5.0, 5.0, 0.0)
    z1 = mlab.bivariate_normal(x, y, 1.0, 2.0, 2.0, 5.0)
    z2 = mlab.bivariate_normal(x, y, 1.7, 1.7, 8.0, 8.0)
    return 50000.0 * z0 + 2500.0 * z1 + 5000.0 * z2

def caldera_sim_function(x, y, map_size=(100,100)):
    warnings.filterwarnings("ignore", category=matplotlib.cbook.MatplotlibDeprecationWarning)
    x, y = x / (map_size[0] / 10.), y / (map_size[1] / 10.)
    z0 = mlab.bivariate_normal(x, y, 10.0, 5.0, 5.0, 0.0)
    z1 = mlab.bivariate_normal(x, y, 1.0, 2.0, 2.0, 5.0)
    z2 = mlab.bivariate_normal(x, y, 1.7, 1.7, 8.0, 8.0)
    return 50000.0 * z0 + 2500.0 * z1 + 5000.0 * z2```




#caldera_Z = caldera_sim_function(X, Y)
print(caldera_sim_function(100, 100))
