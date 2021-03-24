import matplotlib as plt
import netCDF4 as nc
from pylab import *

fn = 'C:/Users/manis/Documents/C321p7DataManagement/anxsondewnpnX11.b1.20200420.231200.cdf'
ds = nc.Dataset(fn)
lenreported = ds.dimensions["time"]#returns string of the number of values, not exactly the brightest idea of mine
a = 'temp'
surfpres = ds[a][:]
alt = ds['alt'][:]
# time = ds['time'][:] #Stores seconds from 12:00 AM -> amt of values can be seen from x
# lendata = len(time)
# for x in range(lendata):
#     time[x] = time[x]/3600
# maxsp = max(surfpres)
# minsp = min(surfpres)
#plt.plot(surfpres, alt)
plt.xlabel(a)
plt.ylabel('Altitude(m)')

#plt.show()


print('End Code')