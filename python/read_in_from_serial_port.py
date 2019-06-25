from time import sleep
import serial
from datetime import datetime as dt

now = dt.now()

print(now)

outfilename = "sensor_data_{0}_{1}_{2}_{3}:{4}:{5}.dat".format(now.year,now.month,now.day,now.hour,now.minute,now.second)
outfile = open(outfilename,'wb')

print(outfilename)

# This part might change if we plug the Arduino into different 
# USB ports or different computers.
# We can get this from the lower right of any Arduino sketch

#ser = serial.Serial('/dev/ttyACM0', 9600) # Establish the connection on a specific port
ser = serial.Serial('/dev/ttyUSB0', 9600) # Establish the connection on a specific port

try:
    while True:
        
        sensor_outputs = ser.readline() # Read the newest output from the Arduino
        print(sensor_outputs)
        outfile.write(sensor_outputs)

        # Need to flush buffer or file will not get written to disc until 
        # we break the loop. 
        outfile.flush()

        #sleep(.1) # Delay for one tenth of a second

# Ctrl-C will break the loop gracefully
except KeyboardInterrupt:
    pass

outfile.close()
