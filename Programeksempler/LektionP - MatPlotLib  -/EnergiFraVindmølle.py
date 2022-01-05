import math

import matplotlib.pyplot as plt
import numpy as np

# 100 linearly spaced numbers
#x = np.linspace(-np.pi,np.pi,100)
x = np.linspace(0,30,100)
# the function, which is y = sin(x) here
m = 1
y = 0.5*m*x**3

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

y1 = 0.333*y
y2 = 0.333*31400*y
# plot the functions
plt.plot(x,y1, 'b', label='Effekt(Watt) fra 1 kvadrats mølle')
plt.plot(x,y2, 'g', label='Effekt(Watt) fra 100 metersvinge mølle')




plt.legend(loc='upper left')

# show the plot
plt.show()
