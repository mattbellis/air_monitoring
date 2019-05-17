import matplotlib.pylab as plt
import numpy as np


x = np.arange(0,1023,1)

v = np.sqrt((10000 * ((x/1023.0) - 0.5))/1.225)

plt.figure()
plt.plot(x,v,'.')

plt.show()
