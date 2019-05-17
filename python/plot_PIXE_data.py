import numpy as np
import matplotlib.pylab as plt

import sys

infilenames = sys.argv[1:]

plt.figure(figsize=(12,5))

for icount,infilename in enumerate(infilenames):
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
    x*=0.028

    #plt.plot(x,vals,'.-',label=infilename,linewidth=3)
    # For paper plot
    # python plot_PIXE_data.py PIXE_data/Ktape_*
    if icount%2==0:
        plt.plot(x,vals,'-',linewidth=3,label='Kapton tape, 0.8 micron filter')
    else:
        plt.plot(x,vals,'--',linewidth=3,label='Kapton tape, 2.5 micron filter')

plt.yscale('log')
plt.xlim(2,5)
#plt.xlim(2,10)
plt.ylim(1,140)
plt.xlabel('Energy [keV]',fontsize=18)
plt.ylabel('Counts',fontsize=18)
ax = plt.gca()
ax.tick_params(axis = 'both', which = 'major', labelsize = 18)

plt.tight_layout()

plt.legend(loc='lower left',fontsize=18)

plt.savefig('pixe_spectrum.png')

plt.show()
