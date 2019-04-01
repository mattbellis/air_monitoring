import numpy as np
import matplotlib.pylab as plt

import sys

################################################################################
def parse_line(line):

    vals = line.split()
    nvals = len(vals)
    if nvals!=15:
        return None

    time = float(vals[0])
    offset0 = float(vals[1])
    bits0 = int(vals[2])
    voltage0 = float(vals[3])
    velsq0 = float(vals[4])
    deltaP0 = float(vals[5])

    offset1 = float(vals[6])
    bits1 = int(vals[7])
    voltage1 = float(vals[8])
    velsq1 = float(vals[9])
    deltaP1 = float(vals[10])

    baro = float(vals[11])
    tempF = float(vals[12])
    tempF2 = float(vals[13])
    humidity = float(vals[14])

    return time, offset0, bits0, voltage0, deltaP0, velsq0, offset1, bits1, voltage1, deltaP1, velsq1, baro, tempF, tempF2, humidity
    


################################################################################

data = {}
data["time"] = [] 
data["offset0"] = [] 
data["bits0"] = [] 
data["voltage0"] = [] 
data["deltaP0"] = [] 
data["velsq0"] = [] 
data["offset1"] = [] 
data["bits1"] = [] 
data["voltage1"] = [] 
data["deltaP1"] = [] 
data["velsq1"] = [] 
data["baro"] = [] 
data["tempF"] = [] 
data["tempF2"] = [] 
data["humidity"] = []

infilename = sys.argv[1]
infile = open(infilename)

for line in infile:
    
    #print(line)
    vals = parse_line(line)
    if vals is not None:
        time, offset0, bits0, voltage0, deltaP0, velsq0, offset1, bits1, voltage1, deltaP1, velsq1, baro, tempF, tempF2, humidity = vals
        data["time"].append(time)
        data["bits0"].append(bits0)
        data["offset0"].append(offset0)
        data["voltage0"].append(voltage0)
        data["deltaP0"].append(deltaP0)
        data["velsq0"].append(velsq0)
        data["bits1"].append(bits1)
        data["offset1"].append(offset1)
        data["voltage1"].append(voltage1)
        data["deltaP1"].append(deltaP1)
        data["velsq1"].append(velsq1)
        data["tempF"].append(tempF)
        data["tempF2"].append(tempF2)
        data["baro"].append(baro)
        data["humidity"].append(humidity)

print(data) 

for key in data.keys():
    data[key] = np.array(data[key])

print(data["velsq0"])
print(data["deltaP0"])

# Convert seconds to minutes
data["time"] = data["time"]/60.0

density_of_air = 1.225 

# MY CALCS
slope = 1.0
data["voltage0"] = (data["bits0"]/1023.0)*5.0
data["deltaP0"] = 1000.0*(data["voltage0"] - data["offset0"])/slope
data["velsq0"] = (2*data["deltaP0"])/density_of_air

data["voltage1"] = (data["bits1"]/1023.0)*5.0
data["deltaP1"] = 1000.0*(data["voltage1"] - data["offset1"])/slope
data["velsq1"] = (2*data["deltaP1"])/density_of_air


#######################
data["vel0"] = data["velsq0"] 
data["vel0"][data["vel0"] < 0.0] = 0
data["vel0"] = np.sqrt(data["vel0"])

data["vel1"] = data["velsq1"] 
data["vel1"][data["vel1"] < 0.0] = 0
data["vel1"] = np.sqrt(data["vel1"])

#exit()

plt.figure(figsize=(14,9))

plt.subplot(3,4,1)
plt.plot(data["time"],data["bits0"],'.')
plt.xlabel("Time (min)",fontsize=12)
plt.ylabel("Bits",fontsize=12)

plt.subplot(3,4,2)
plt.plot(data["time"],data["voltage0"],'.',label='Voltage')
plt.plot(data["time"],data["offset0"],'.',label='Offset')
plt.xlabel("Time (min)",fontsize=12)
plt.ylabel("Voltage (V)",fontsize=12)
plt.legend()

plt.subplot(3,4,3)
plt.plot(data["time"],data["deltaP0"],'.')
plt.xlabel("Time (min)",fontsize=12)
plt.ylabel(r"$\Delta P$ (Pa)",fontsize=12)

plt.subplot(3,4,4)
#plt.plot(data["time"],data["velsq0"],'.',label=r'Velocity$^2$')
plt.plot(data["time"],data["vel0"],'.',label=r'Velocity')
plt.xlabel("Time (min)",fontsize=12)
plt.ylabel(r"V/V$^2$ (m/s or m$^2$/s$^2$)",fontsize=12)
plt.legend()

#################

plt.subplot(3,4,5)
plt.plot(data["time"],data["bits1"],'.')
plt.xlabel("Time (min)",fontsize=12)
plt.ylabel("Bits",fontsize=12)

plt.subplot(3,4,6)
plt.plot(data["time"],data["voltage1"],'.',label='Voltage')
plt.plot(data["time"],data["offset1"],'.',label='Offset')
plt.xlabel("Time (min)",fontsize=12)
plt.ylabel("Voltage (V)",fontsize=12)
plt.legend()

plt.subplot(3,4,7)
plt.plot(data["time"],data["deltaP1"],'.')
plt.xlabel("Time (min)",fontsize=12)
plt.ylabel(r"$\Delta P$ (Pa)",fontsize=12)

plt.subplot(3,4,8)
#plt.plot(data["time"],data["velsq1"],'.',label=r'Velocity$^2$')
plt.plot(data["time"],data["vel1"],'.',label=r'Velocity')
plt.xlabel("Time (min)",fontsize=12)
plt.ylabel(r"V/V$^2$ (m/s or m$^2$/s$^2$)",fontsize=12)
plt.legend()


plt.subplot(3,4,9)
plt.plot(data["time"],data["tempF"],'.')
plt.xlabel("Time (min)",fontsize=12)
plt.ylabel("Temperature (F)",fontsize=12)

plt.subplot(3,4,10)
plt.plot(data["time"],data["baro"],'.')
plt.xlabel("Time (min)",fontsize=12)
plt.ylabel("Barometric pressure (kPa)",fontsize=12)

plt.subplot(3,4,11)
plt.plot(data["time"],data["humidity"],'.')
plt.xlabel("Time (min)",fontsize=12)
plt.ylabel("Humidity (???)",fontsize=12)

plt.tight_layout()




plt.figure()
#plt.plot(data["time"],data["vel0"]-data["vel1"],'.',label=r'Velocity 0')
plt.plot(data["time"],data["vel0"],'.',label=r'Velocity 0')
plt.plot(data["time"],data["vel1"],'.',label=r'Velocity 1')
plt.xlabel("Time (min)",fontsize=12)
#plt.ylabel(r"V/V$^2$ (m/s or m$^2$/s$^2$)",fontsize=12)
plt.ylabel(r"V (m/s)",fontsize=12)
plt.legend()


plt.show()



