import random
import serial
import time
import math
def main():

    i = 0
    while True:
        file = open("sampleText.txt",'a+')
        # data = time.strftime('%H:%M:%S')+" "+str(math.sin(i%(2*math.pi)))+"\n"
        data = time.strftime('%H:%M:%S')+" "+str( 200*math.exp(-0.05*i)*math.sin(i))+"\n"
        file.write(data)
        print(data)
        file.close() 
        i += 0.2
        time.sleep(0.5)

main()