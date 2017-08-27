import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime

fig = plt.figure()
# plt.rc('axes', titlesize=8)
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 1, 2)
ax1.set_title('wire1')
ax1.set_xlabel('time')
ax1.set_ylabel('Reflection Coefficient1')

ax2.set_title('wire2')
ax2.set_xlabel('time')
ax2.set_ylabel('Reflection Coefficient2')

ax3.set_title('wire3')
ax3.set_xlabel('time')
ax3.set_ylabel('Reflection Coefficient3')

def animate(k):
    i = 0 
    pullData = open("sampleText.txt", "r").read()
    dataArray = pullData.split('\n')
    xar, xa1, xa2 = [], [], []
    yar, ya1, ya2 = [], [], []
    for eachLine in dataArray:
        if len(eachLine) > 1:
            x,y = eachLine.split(' ')
            if i%3 == 0:
                yar.append(float(y))
                xar.append(datetime.strptime(x, '%H:%M:%S'))
            if i%3 == 1:
                ya1.append(float(y))
                xa1.append(datetime.strptime(x, '%H:%M:%S'))
            if i%3 == 2:
                ya2.append(float(y))
                xa2.append(datetime.strptime(x, '%H:%M:%S'))            
            i += 1
    ax1.plot_date(xar, yar, linestyle='-')
    ax2.plot_date(xa1, ya1, linestyle='-', color='b')
    ax3.plot_date(xa2, ya2, linestyle='-', color='g')
 
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
