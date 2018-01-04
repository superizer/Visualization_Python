import random
import numpy as np
import pylab as plt
import matplotlib.animation as animation
'''
list_x = []
list_y = []
for i in range(10):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    list_x.append(x)
    list_y.append(y)
    print(list_x,list_y)


plt.plot(list_x, list_y, 'ro')
plt.show()
'''

list_x = [1,2,3,4,5]
list_y = [1,2,3,4,5]

def animate(frameno):
    #pass
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    list_x.append(x)
    list_y.append(y)
    print(list_x,list_y)


fig, ax = plt.subplots()
plt.plot(list_x, list_y, 'ro')
ani = animation.FuncAnimation(fig, animate, np.arange(1, 10), blit=False, interval=10,
                              repeat=True)
plt.show()
