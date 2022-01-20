import matplotlib.pyplot as plt
import numpy as np


"""print("Du skal nu indtaste de  3 værdier a,b,c for den ene ligning med 2 ubekendte")
print("eksempelvis x*a + y*b = c")
a = input("Indtast nu værdien for a")
b = input("Indtast nu værdien for b")
c = input("Indtast nu værdien for c")

print("Du skal nu indtaste de  3 værdier a,b,c for den anden ligning med 2 ubekendte")
print("eksempelvis x*a + y*b = c")
d = input("Indtast nu værdien for d")
e = input("Indtast nu værdien for e")
f = input("Indtast nu værdien for f")
"""

a = 1
b = 1
c = 5

d = -1
e = 1
f = 2





# 100 linearly spaced numbers

x1 = (np.linspace(-10, 10, 100))
y1 = (c-(x1*a))/b

x2 = (np.linspace(-10, 10, 100))
y2 = (f-(x2*d))/e




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
plt.plot(x1, y1, 'r', label='ligning 1')
plt.plot(x2, y2, 'b', label='ligning 2')

plt.legend(loc='upper left')

# show the plot
plt.show()


