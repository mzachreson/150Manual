# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 15:29:11 2017

@author: matthewz
"""


from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import numpy as np
#import matplotlib.mlab as mlab
import math

mu = 0
variance = 4
sigma = math.sqrt(variance)
x = np.linspace(-10, 10, 100)
# example data
x = 0.5
y = 0.1

# example variable error bar values
yerr = 0.1 + 0.2*np.sqrt(x)
xerr = 0.1 + yerr



myFig=plt.errorbar(x, y, xerr=0.6, yerr=0.1,fmt='o')

#ax=plt.subplot(111)
ax=plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.set_xlim([-0.2, 1])
ax.set_ylim([0, 0.5])

pp = PdfPages('multipage.pdf')
pp.savefig()
pp.close()

plt.show()