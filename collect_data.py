# import sounddevice as sd #pip install sounddevice
import numpy as np
import serial
import io
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
# sd.default.channels = 2
ser = serial.Serial('COM3', 57600)
# ser.open()
# ans = 0
#file = open("testfile.txt","w") 
 
def main():
    k = 0
    # file = open("newfiletdrdata.txt",'a')
    while True:
        file = open("newfiletdrdata.txt",'a')
        data = ser.readline().decode('UTF-8').strip().split("=")
        file.write(str(k)+" "+data[1][1:]+"\n")
        print(k,data[1][1:])
        k += 1
        file.close() 
main()

#     file = open("sampleText.txt",'w+')
#     while True:
#         data = str(random.uniform(-1,1))+" "+str(random.uniform(-1,1))+"\n"
#         file.write(data)
#         print(data)
#         time.sleep(.01)
#     file.close() 
# main()