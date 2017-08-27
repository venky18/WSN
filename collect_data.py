import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

ser = serial.Serial('COM3', 57600)
if not ser.is_open:
    ser.open()

def main():
    k = 0
    while True:
        file = open("newfiletdrdata.txt", 'a+')
        data = ser.readline().decode('UTF-8').strip().split("=")
        formatted_data = time.strftime('%H:%M:%S') + " " + data[1][1:] + "\n"
        file.write(formatted_data)
        print(formatted_data)
        file.close()


main()
