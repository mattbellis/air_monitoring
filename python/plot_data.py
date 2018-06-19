import numpy as np
import matplotlib.pylab as plt

import sys

infilename = sys.argv[1]
infile = open(infilename,'r')

vel = []
for line in infile:
    print(line)
    vals = line.split()
    if len(vals)==7:
        vel.append(float(vals[3]))

time = np.linspace(0,2*len(vel),len(vel))
vel = np.array(vel).astype(float)

time = time[vel==vel]
vel = vel[vel==vel]

print(vel)


plt.figure()
plt.plot(time,vel,'.')
plt.ylim(0,20)

plt.show()



