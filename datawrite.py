import time
import random
def main():

    i = 0
    while True:
        file = open("sampleText.txt", 'a+')
        data = time.strftime('%H:%M:%S')+" "+str(random.uniform(0.2, 0.5))+"\n"
        # data = time.strftime('%H:%M:%S') + " " + str(int(random.uniform(0.2, 0.5))) + "\n"
        # data = time.strftime('%H:%M:%S')+" "+str( 200*math.exp(-0.05*i)*math.sin(i))+"\n"
        file.write(data)
        print(data)
        file.close() 
        i += 0.2
        time.sleep(0.5)

main()
