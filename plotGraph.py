import matplotlib.pyplot as plt
import matplotlib.animation as animation
# import random
# def main():
#     file = open("sampleText.txt",'w')
#     # data = ser.readline().decode('UTF-8')
#     while True:
#         data = str(random.randint(1,10))+" "+str(random.randint(2,20))+"\n"
#         file.write(data)
#         print(data)
#     file.close() 

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(k):
    i = 0 
    pullData = open("newfiletdrdata.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(' ')
            xar.append(i)
            yar.append(float(y))
            i+=1
    ax1.clear()
    ax1.plot(xar,yar)

ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()