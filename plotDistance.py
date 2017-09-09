import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 1, 2)

def reset_ax1():
    ax1.set_title('wire1')
    ax1.set_xlabel('time')
    ax1.set_ylabel('displacement 1 ')
    ax1.set_xlim(0,100)
    # ax1.set_xticks(range(100), minor=True)
    # ax1.set_xticklabels(range(100))

ax2.set_title('wire2')
ax2.set_xlabel('time')
ax2.set_ylabel('displacement 2')

ax3.set_title('wire3')
ax3.set_xlabel('time')
ax3.set_ylabel('displacement 3')


def animate(k):
    i = 0
    pullData = open("sampleText.txt", "r").read()
    dataArray = pullData.split('\n')
    xa0, xa1, xa2 = [], [], []
    ya0, ya1, ya2 = [], [], []
    for eachLine in dataArray:
        if len(eachLine) > 1:
            x, y = eachLine.split(' ')
            if i % 3 == 0:
                ya0.append(1+float(y)/0.1)
                xa0.append(i)
                # xa0.append(datetime.strptime(x, '%H:%M:%S'))
            if i % 3 == 1:
                ya1.append(1+float(y)/0.1)
                xa1.append(i)
                # xa1.append(datetime.strptime(x, '%H:%M:%S'))
            if i % 3 == 2:
                ya2.append(1+float(y)/0.1)
                xa2.append(i)
                # xa2.append(datetime.strptime(x, '%H:%M:%S'))
            i += 1
            if i%100 == 0:
                ax1.clear()
                reset_ax1()
                ya0,xa0 = [],[]
                i = 0
    ax1.plot(xa0, ya0, linestyle='-', color='crimson')
    ax2.plot(xa1, ya1, linestyle='-', color='midnightblue')
    ax3.plot(xa2, ya2, linestyle='-', color='coral')


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
