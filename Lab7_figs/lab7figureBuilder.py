# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 11:03:00 2017

@author: matthewz
"""


import matplotlib.pyplot as plt
from matplotlib import lines as mpl_lines
import numpy as np


#Set up two functions for easy line plotting
def slope_from_points(point1, point2):
    return (point2[1] - point1[1])/(point2[0] - point1[0])

def plot_secant(point1, point2, ax):
    # plot the secant
    slope = slope_from_points(point1, point2)
    intercept = point1[1] - slope*point1[0] 
    # update the points to be on the axes limits
    x = ax.get_xlim()
    y = ax.get_ylim()
    data_y = [x[0]*slope+intercept, x[1]*slope+intercept]
    line = mpl_lines.Line2D(x, data_y, color='blue', linestyle='-', linewidth=1.5)
    ax.add_line(line)
    return ax.figure()
    


#Now build each of the images
max_t=6 #maximum time in seconds
plot_dt=0.1
t=np.arange(0,max_t+plot_dt,plot_dt)
v0=5
a=-2*v0/max_t
x0=0
#Now get x and v as function of time
v=v0+a*t
x=x0+v0*t+0.5*a*t**2

#Position graph
plt.plot(t,x,linewidth='2.5',color='green')
plt.ylabel('Position (m)',fontsize=16)
plt.xlabel('time (s)',fontsize=16)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.savefig('PvTsimple.svg',close=False)

ax=plt.gca()

plot_secant([0,0],[1,v0*1],ax)

