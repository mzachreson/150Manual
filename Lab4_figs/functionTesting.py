from lab4Source1 import *
    
    


import numpy as np



#xdata = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
#ydata = [320, 547, 874, 1570, 2062, 1862, 2800, 2700, 2740, 3220]
xdata=[1,2,3,4,5,6]
ydata=[1,2,3,4,5,6]
[slope,slopeErr], [intercept,interceptErr] = linearLeastSquares(xdata,ydata)
print('Slope: {}+/-{}'.format(slope,slopeErr))
print('Intercept: {}+/{}'.format(intercept,interceptErr))