import netCDF4 as nc
from pylab import *
import numpy
import os
import pandas as pd


fn = 'C:/Users/manis/Documents/C321p7DataManagement/sonde/anxinterpolatedsondeM1.c1.20200420.000030.nc'
ds = nc.Dataset(fn)
height = ds['height'][:]
temp = ds['temp'][:] #2DArray
vappres = ds['vap_pres'][:]
barpres = ds['bar_pres'][:]
time = ds['time'][:]
tempavg = []
vapavg = []
baravg = []
for a in range(0, len(height)): #through rows
    sumtemp = 0
    sumvap=0
    sumbar = 0
    for b in range(0, len(time)):
        sumtemp = sumtemp+temp[b][a]
        sumvap = sumvap + vappres[b][a]
        sumbar = sumbar + barpres[b][a]
    tempavg.append(sumtemp/len(time))
    vapavg.append(sumvap / len(time))
    baravg.append(sumbar / len(time))

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
fig.suptitle("Vertical Profiles for Vapor & Bar Pressure & Temperature")
ax1.plot(tempavg, height)
ax1.set(xlabel='Temperature', ylabel='Height in km')
ax2.plot(vapavg, height)
ax2.set(xlabel='Vapor Pressure')
ax3.plot(baravg, height)
ax3.set(xlabel='Barometric Pressure')

# varnames = ['temp', 'vap_pres', 'bar_pres']
# VertProfs = [[]]
# count=0
# for a in varnames:
#     Blue = []
#     #Blue.append(a)
#     R = ds[a][:]
#     for b in range(1, len(height)):
#         sum1 = 0
#         count+=1
#         for c in range(1, len(time)):
#             sum1 = sum1 + R[c][b]
#         Blue.append(sum1 / len(time))
#     VertProfs.append(Blue)
# VertProfs.pop(0)
# fig, axs = plt.subplots(1, len(varnames))
# fig.suptitle("Vertical Profiles")
# for i in range(0, len(varnames)):
#     axs[0,i].plot[VertProfs[i],height]
#     axs[0,i].set(xlabel=varnames[i])
# axs[0,0].set(ylabel="Height(km)")
