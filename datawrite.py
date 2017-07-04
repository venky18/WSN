import random
import serial
import time
def main():
    file = open("sampleText.txt",'w+')
    # data = ser.readline().decode('UTF-8')
    while True:
        data = str(random.uniform(-1,1))+" "+str(random.uniform(-1,1))+"\n"
        file.write(data)
        print(data)
        time.sleep(.01)
    file.close() 
main()