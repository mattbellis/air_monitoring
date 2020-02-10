import numpy as np
import matplotlib.pylab as plt

import sys

from xray_data import elements

import scipy.stats as stats

from scipy.optimize import approx_fprime,fmin_bfgs
from scipy.integrate import dblquad

from lichen.fit import Parameter,get_numbers,reset_parameters,pois,errfunc,pretty_print_parameters,get_values_and_bounds,fit_emlm
import lichen as lch
import lichen.pdfs as pdfs

################################################################################
def background(pars, x, frange=None, key=None,subnormranges=None):

    k0 = pars[key]["k0"].value
    k1 = pars[key]["k1"].value
    k2 = pars[key]["k2"].value

    ypredict = k0 + k1*x[0] + k2*x[0]*x[0]

    return ypredict
################################################################################



infilenames = sys.argv[1:]

plt.figure(figsize=(12,5))

maxval = 0

x, vals = None, None

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
    #vals /= live_time
    x = np.linspace(0,len(vals),len(vals))
    x *= slope
    x += intercept

    if max(vals)>maxval:
        maxval = max(vals)

    #plt.plot(x,vals,'.-',label=infilename,linewidth=3)
    # For paper plot
    # python plot_PIXE_data.py PIXE_data/Ktape_*
    #plt.plot(x,vals,'-',linewidth=3,label=filelabel)
    plt.plot(x,vals,'.',linewidth=3,label=filelabel)

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

plt.tight_layout()

#plt.legend(loc='lower left',fontsize=18)
plt.legend(fontsize=12)

plt.savefig('pixe_spectrum_FIT.png')

plt.show()
