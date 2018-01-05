# -*- coding: utf-8 -*-
"""
One Dimensional free-fall Euler Code

PH150
Brother Zachreson


This code will calculate the exact solution for a ball in free fall
having been shot straight up using Euler's method.

"""
#Import numerical and plotting packages
import numpy as np
import matplotlib.pyplot as plt


#Initial conditions and physical setup constants
v0=30.0 #Initial velocity in m/s
x0=70 #Initial Postion in m

#Set up the time steps and number of calculations
delta_t = 0.01 #Time step in seconds
t0=0 #Start time in seconds
t_max = 7.0 #Final time

#Calculate the number of timesteps we need to make
N=(t_max-t0)/delta_t

#Make sure N is an integer
N=int(N)


#Make lists to hold our positions, velocities, and times
x=[x0]
v=[v0]
t=[t0]

#Now perform an Euler's method calculation.
for i in range(N):
    #Find the current acceleration
    g=-9.8
    
    #Find the next velocity
    v.append(v[i]+g*delta_t)    
    
    
    #Find the next position
    x.append(x[i]+v[i]*delta_t)
    
    #increment our time
    t.append(t[i]+delta_t)

#End of Euler loop =========================================
#Plot the results
plt.plot(t,x,linewidth=2,color='red')
plt.xlabel('time (s)')
plt.ylabel('Position (m)')
plt.title('Position vs. time for a ball in free fall')


    