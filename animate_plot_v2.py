import random
import pylab as plt

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
