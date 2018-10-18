import numpy as np
import matplotlib.pylab as plt

import sys

infilenames = sys.argv[1:]

plt.figure()

for infilename in infilenames:
    data = open(infilename,encoding = "ISO-8859-1").readlines()

    live_time = float(data[7].split()[-1])
    print(live_time)

    #print(data[16:1040])
    vals = []
    for i in data[16:1040]:
        vals.append(float(i.strip()))

    vals = np.array(vals)
    vals /= live_time
    x = np.linspace(0,len(vals),len(vals))
    #print(x)
    x*=0.031

    plt.plot(x,vals,'.',label=infilename)

plt.yscale('log')
plt.xlim(0.5, 5.0)
plt.legend()

plt.show()
