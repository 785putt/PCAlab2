import serial
from datetime import datetime
import time
import keyboard

sampleTime = '1000'
speed_of_sound = 165
# Sampling Tin
timelist = [0]
distancelist = [0]
index = 0

with serial.Serial('COM10', 9600) as serArd:
    print("The Arduino board is connect through", serArd.port)
    time.sleep(2)
    serArd.reset_input_buffer()

    if (serArd.writable()):
        serArd.write(sampleTime.encode())
        print(serArd.readline().decode().rstrip())
    while not keyboard.is_pressed('q'):
        if (serArd.inWaiting() > 0):
            rec_time = datetime.now().strftime('%H:%M: %S.%f')
            timelist.append(float(rec_time[8:]))
            index += 1
            myData = serArd.readline().decode().rstrip()
            try:
                myData = float(myData)
                distance = myData*178*(10**-4)
                distancelist.append(float(distance))
                if distance < 3:
                    print("raw data at",rec_time,": clear")
                else:
                    print("raw data at",rec_time,":",myData*178*(10**-4),"cm")
                    timepass = timelist[index] - timelist[index -1]
                    distancechange = distancelist[index] - distancelist[index - 1]
                    if distancechange > 1:
                        print("speed = ", distancechange/abs(timepass), "cm/s backwards" )
                    if distancechange < -1:
                        print("speed = ", abs(distancechange) / abs(timepass), "cm/s fowards")
                    else:
                        print("speed = ", 0, "cm/s")

            except:
                print("No data")
            '''
            rec_time = datetime.now().strftime('%H:%M:%S.%f')
            myData = serArd.readline().decode().rstrip()
            aData = ((int(myData) * 10**-6) *  speed_of_sound) * 100
            try:
                myData = float(myData)
                print("raw data at", rec_time,':',myData)
                print("aData at", rec_time,':',aData,'cm')
            except:
                print("No data")
            '''
