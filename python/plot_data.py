import numpy as np
import matplotlib.pylab as plt

import sys

infilename = sys.argv[1]
infile = open(infilename,'r')

vel = []
for line in infile:
    #print(line)
    vals = line.split()
    if len(vals)>=7:
        V = float(vals[1])
        offset = float(vals[0])

        sig = V*2.5/1024.0 
        dP = sig*1000
        print(dP, " Pa")


        #dV = V-offset
        #dP = 1000*dV
        v = np.sqrt(dP*2/1.225)
        #print(v,float(vals[4]))
        #vel.append(float(vals[4]))
        vel.append(v)

time = np.linspace(0,2*len(vel),len(vel))
vel = np.array(vel).astype(float)

time = time[vel==vel]
vel = vel[vel==vel]

#print(vel)


plt.figure()
plt.plot(time,vel,'.')
plt.ylim(0,20)

plt.show()



