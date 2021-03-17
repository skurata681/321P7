import matplotlib as plt
import netCDF4 as nc
from pylab import *

fn = 'C:/Users/manis/Documents/C321Project_Local/mwrret1liljclou/anxmwrret1liljclouM1.c2.20191201.000000.nc'
ds = nc.Dataset(fn)
varnames = []
for a in ds.variables:
    varnames.append(a)
lenrick = len(varnames) #calculate averages for what we need
avgdata = []
time = ds['time'][:]
lendata = len(time)
for a in range(4, lenrick-7):
    surfpres = ds[varnames[a]][:]
    avgpres = sum(surfpres) / lendata
    avgdata.append(avgpres)
print(varnames[4:lenrick-7])
print(avgdata)
# lenreported = ds.dimensions["time"] #returns string of the number of values, not exactly the brightest idea of mine
# surfpres = ds['surface_pres'][:]
# time = ds['time'][:] #Stores seconds from 12:00 AM -> amt of values can be seen from x
# lendata = len(time)
# for x in range(lendata):
#     time[x] = time[x]/3600
# maxsp = max(surfpres)
# minsp = min(surfpres)
# plt.plot(time, surfpres)
# plt.ylabel('Surface Pressure(kPa)')
# plt.xlabel('Time(hours since 12:00 AM)')
# plt.title('Surface Pressure on 12/1/2019')
# plt.axis([-0.5, 24.5, minsp-0.05, maxsp+0.05])
# plt.show()


print('End Code')