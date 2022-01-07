import matplotlib.pyplot as plt
import numpy as np

# 100 linearly spaced numbers

x = np.linspace(-np.pi, np.pi, 1000000)

# the function, which is y = sin(x)
y = np.sin(x)
mystisk = (np.sin(x*500)/300)+(np.sin(x*2000)/1000)+(np.sin(x*20000)/10000)+(np.sin(x*200000)/100000)+0.0001

#mystisk = (np.sin(x*500)/300)+(np.sin(x*2000)/1000)+0.0001

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x, y, 'r', label='En sinus funktion')
plt.plot(x, y / 2, 'b', label='En sinus/2 funktion')
plt.plot(x,(x+mystisk),"g", label = "test")
plt.legend(loc='upper left')

# show the plot
plt.show()


