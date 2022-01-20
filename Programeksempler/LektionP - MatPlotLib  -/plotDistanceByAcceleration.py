import matplotlib.pyplot as plt
import numpy as np

#plotDistanceByAcceleration.py
# 100 linearly spaced numbers
x = np.linspace(0,10,100)

# the function, which is y = x^2 here
y = 0.5*9.82*pow(x,2)

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x,y, 'r', label = "Distance[meters]")
plt.legend(loc='upper left')
plt.grid()
# show the plot
plt.show()

