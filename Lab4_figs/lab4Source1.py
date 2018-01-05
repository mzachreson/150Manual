# -*- coding: utf-8 -*-




'''
This Function takes in a set of x and

'''

def linearLeastSquares(x,y):
    #Import numpy
    import numpy as np
    #Get the number of data points
    N=len(x)

    #Make sure x and y are numpy arrays to make array math easy
    x=np.asarray(x)
    y=np.asarray(y)

    #Calculate the average values needed to find the slope and intercept
    xbar=np.mean(x) #Average Value of the xdata
    ybar=np.mean(y) #Average value of the y data
    xbar2=np.mean(x**2) #Average value of the xdata squared
    xybar=np.mean(x*y) #Average value of xdata*ydata



    #Use the linear least squares formula to calculate
    #the slope and the intercept of the best fit line
    slope=(xybar-xbar*ybar)/(xbar2-xbar**2)
    intercept=ybar-slope*xbar

    #This section estimates the error in the fit =========================

    #Calculate the variance in the fit
    #Calculate the stuff inside the sum first to make the code easier to read
    sigmaYinsideSum = np.square(y-intercept-slope*x)

    #Get the uncertaintiy in the measurements (variance)
    sigmaY=np.sqrt(np.sum(sigmaYinsideSum)/(N-2))

    #Now calculate the error in the slope and intercept
    sigmaSlope = sigmaY/np.sqrt(N*(xbar2-xbar**2))
    sigmaIntercept = sigmaY*np.sqrt(xbar2/(N*(xbar2-xbar**2)))






    #End of error estimating section =====================================

    #Now return the slope and intercept, with their error as a list of lists


    return [
           [slope,sigmaSlope],
           [intercept,sigmaIntercept]
           ]

def linearLeastSquares_noIntercept(x,y):
    #Import numpy
    import numpy as np
    #Get the number of data points
    N=len(x)

    #Make sure x and y are numpy arrays to make array math easy
    x=np.asarray(x)
    y=np.asarray(y)

    #Calculate the average values needed to find the slope and intercept
    xbar2=np.mean(x**2) #Average value of the xdata squared
    xybar=np.mean(x*y) #Average value of xdata*ydata



    #Use the linear least squares formula to calculate
    #the slope and the intercept of the best fit line
    slope=xybar/xbar2


    #This section estimates the error in the fit =========================

    #Calculate the variance in the fit
    #Calculate the stuff inside the sum first to make the code easier to read
    sigmaYinsideSum = np.square(y-slope*x)

    #Get the uncertaintiy in the measurements (variance)
    sigmaY=np.sqrt(np.sum(sigmaYinsideSum)/(N-1))

    #Now calculate the error in the slope and intercept
    sigmaSlope = sigmaY/np.sqrt(xbar2)







    #End of error estimating section =====================================

    #Now return the slope and intercept, with their error as a list of lists


    return slope,sigmaSlope




import numpy as np



xdata = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
ydata = [320, 547, 874, 1570, 2062, 1862, 2800, 2700, 2740, 3220]
#ydata=[0.9,2.1,3,3.85,5.15,5.95]
#xdata=[1,2,3,4,5,6]
[slope,slopeErr], [intercept,interceptErr] = linearLeastSquares(xdata,ydata)


fit_params=linearLeastSquares(xdata,ydata)
slope_params, intercept_params =linearLeastSquares(xdata,ydata)
[slope,slopeErr], [intercept,interceptErr] = linearLeastSquares(xdata,ydata)
#slope,slopeErr = linearLeastSquares_noIntercept(xdata,ydata)
#intercept,interceptErr=0,0
#Build Figures for lab four manual
import matplotlib.pyplot as plt
#Get high, low, and fitted data
fit_y=slope*np.asarray(xdata)+intercept
high_y=(slope+slopeErr)*np.asarray(xdata)+intercept+interceptErr
low_y=(slope-slopeErr)*np.asarray(xdata)+intercept-interceptErr

#Start with a simple data scatterplot
plt.figure(figsize=(4,2.5))
plt.scatter(xdata,ydata,marker='.',s=100)
plt.xlabel('X values')
plt.ylabel('Y values')
plt.tight_layout()
plt.savefig('dataScatter.pdf')
plt.close()

#Data with fitted line and vertical lines marking offsets
plt.figure(figsize=(4,2.5))
plt.scatter(xdata,ydata,marker='.',s=100)

#plt.plot(xdata,high_y,color='red')
#plt.plot(xdata,low_y,color='red')

#Reorganize lists for plotting vertical lines
xforPlot=[[x,x] for x in xdata]
yforPlot=list(zip(fit_y,ydata))
#Now plot the vertical lines:
for x,y in zip(xforPlot,yforPlot):
    plt.plot(x,y,color='green',linewidth=1.5)
plt.plot(xdata,fit_y,linewidth=2)
plt.scatter(xdata,ydata,marker='.',s=100)
plt.xlabel('X values')
plt.ylabel('Y values')
plt.tight_layout()
plt.savefig('dataWfit.pdf')
plt.close()

#Make a plot of the Data with high/low values of fit
plt.figure(figsize=(4,2.5))
plt.scatter(xdata,ydata,marker='.',s=100)
plt.plot(xdata,fit_y,linewidth=2)
plt.plot(xdata,high_y,color='red')
plt.plot(xdata,low_y,color='red')
plt.xlabel('X values',{'size':14})
plt.ylabel('Y values')
plt.tight_layout()
plt.savefig('dataWfitRange.pdf')
plt.close()



#Now build the other plots - distance vs time vs. distance vs times squared
t=np.arange(0,1.1,0.1)
x=0.5*9.8*t**2
plt.figure(figsize=(4,2.5))
plt.scatter(t,x,marker='.',s=100)

plt.xlabel('time (s)')
plt.ylabel('Fall distance (m)')
plt.tight_layout()
plt.savefig('yvst.pdf')
plt.close()


t=np.arange(0,1.1,0.1)
x=0.5*9.8*t**2
plt.figure(figsize=(4,2.5))
plt.scatter(t**2,x,marker='.',s=100)

plt.xlabel('time^2 (s^2)')
plt.ylabel('Fall distance (m)')
plt.tight_layout()
plt.savefig('yvst2.pdf')
plt.close()
