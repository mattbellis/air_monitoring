import numpy as np
import matplotlib.pylab as plt

import sys

from xray_data import elements

infilenames = sys.argv[1:]

plt.figure(figsize=(12,5))

maxval = 0

for icount,infilename in enumerate(infilenames):
    data = open(infilename,encoding = "ISO-8859-1").readlines()

    filelabel = infilename.split('/')[-1]

    live_time = float(data[7].split()[-1])
    print(live_time)

    # Calibration
    calib_labels = np.array([int(data[13].split()[0]), int(data[14].split()[0])])
    print(calib_labels)
    calib_channels = np.array([float(data[13].split()[-1]), float(data[14].split()[-1])])
    print(calib_channels)

    slope = (calib_channels[1] -  calib_channels[0])/(calib_labels[1] - calib_labels[0])
    intercept1 = calib_channels[1] - calib_labels[1]*slope
    intercept0 = calib_channels[0] - calib_labels[0]*slope
    print(slope,intercept1,intercept0)
    intercept = (intercept1 + intercept0)/2


    # Find where data starts
    idx = -1
    for i,d in enumerate(data):
        if d.find('<<DATA>>')>=0:
            idx = i
    print(idx)

    #print(data[16:1040])
    vals = []
    for i in data[idx+1:1024+idx+1]:
        vals.append(float(i.strip()))

    vals = np.array(vals)
    vals /= live_time
    x = np.linspace(0,len(vals),len(vals))
    #print(x)
    #x*=0.028
    x *= slope
    x += intercept

    if max(vals)>maxval:
        maxval = max(vals)

    #plt.plot(x,vals,'.-',label=infilename,linewidth=3)
    # For paper plot
    # python plot_PIXE_data.py PIXE_data/Ktape_*
    plt.plot(x,vals,'-',linewidth=3,label=filelabel)
    '''
    if icount%2==0:
        plt.plot(x,vals,'-',linewidth=3,label='Kapton tape, 0.8 micron filter')
    else:
        plt.plot(x,vals,'--',linewidth=3,label='Kapton tape, 2.5 micron filter')
    '''

plt.yscale('log')
#plt.xlim(2,5)
#plt.xlim(2,10)
#plt.xlim(2,15)
#plt.xlim(10,15)
#plt.ylim(0.01,140)
plt.xlabel('Energy [keV]',fontsize=18)
plt.ylabel('Counts',fontsize=18)
ax = plt.gca()
ax.tick_params(axis = 'both', which = 'major', labelsize = 18)

print("maxval: ",maxval)
# Plot some elements
elements_to_plot = ['Al', 'Si', 'Cl', 'K', 'Ca', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Cu']

colors = ['r','k','b','g','y','m']

#'''
for ic,e in enumerate(elements_to_plot):
    xrays = elements[e]
    for i,xray in enumerate(xrays):
        xray /= 1000.
        if xray<13 and xray>1.:
            if i==0:
                plt.plot([xray,xray],[0.001,1.2*maxval],'--',label=e,color=colors[ic%len(colors)])
            else:
                plt.plot([xray,xray],[0.001,1.2*maxval],'--',color=colors[ic%len(colors)])
#'''

plt.tight_layout()

#plt.legend(loc='lower left',fontsize=18)
plt.legend(fontsize=12)

plt.savefig('pixe_spectrum.png')

plt.show()
