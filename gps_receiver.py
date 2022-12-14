#   Jose Jesus Sanchez Gomez

#   GPS Receiver: This program reads data from Serial Port in NMEA_0183 format. 
#   The data received is then saved to a file for debugging purposes
#
#   https://www.sparkfun.com/datasheets/GPS/NMEA%20Reference%20Manual-Rev2.1-Dec07.pdf

import serial
import datetime

NUMBER_OF_SAMPLES = 2500

gpsRecv = serial.Serial("/dev/ttyUSB0", 4800, timeout=2)
gpsRecv.readline()

dataFile = open("gpsdatafromcoldstart.txt", "w")

for cont in range(NUMBER_OF_SAMPLES):
    actTime = datetime.datetime.now()
    
    rcvBytes = gpsRecv.readline()
    rcvData = rcvBytes.decode("UTF-8")
    rcvData = rcvData.replace("\r", "")
    rcvData = rcvData.replace("\n", "")

    printTime = actTime.strftime("%H") + ":" + actTime.strftime("%M") + ":" + actTime.strftime("%S") + "." + actTime.strftime("%f")
    dataFile.write(printTime + rcvData + "\n")
    
    if cont % 10 == 0:
        print ("Status: ", cont, "/", NUMBER_OF_SAMPLES)
        
    cont += 1
    
dataFile.close()