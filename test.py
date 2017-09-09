import matplotlib.pyplot as plt
import time
import math
import random
from collections import deque

a1 = deque([0]*30)
ax = plt.axes(xlim=(0, 20), ylim=(0, 10))

line, = plt.plot(a1)
plt.ion()
plt.ylim([-2,2])
plt.show()
i = 0
for i in range(0, 200):
    a1.append(math.sin(i))
    print(a1)
    datatoplot = a1.popleft()
    line.set_ydata(a1)
    plt.draw()
    i += 0.2
    time.sleep(0.1)
    plt.pause(0.0001)
