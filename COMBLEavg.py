import matplotlib as plt
import netCDF4 as nc
from pylab import *
import numpy
import os

directory = os.fsencode('C:/Users/manis/Documents/C321Project_Local/mwrret1liljclou/')
fn = 'C:/Users/manis/Documents/C321Project_Local/mwrret1liljclou/'
avgpresarr = []
dates = []
for file in os.listdir(directory):
    fn = 'C:/Users/manis/Documents/C321Project_Local/mwrret1liljclou/'
    filename = os.fsdecode(file)
    fn += filename
    ds = nc.Dataset(fn)
    surfpres = ds['surface_pres'][:] #getting data
    lendata = len(surfpres)
    avgpres = sum(surfpres) / lendata #calculating avgerage pressure of the day
    avgpresarr.append(avgpres)
    date = filename[26:32]
    date = date[2]+date[3]+"/"+date[4]+date[5] + "/" + date[0]+ date[1] #formatting date in standard format
    dates.append(date)
#print(avgpresarr)
print(filename[26:32])
plt.plot(dates, avgpresarr)
plt.ylabel('Average Daily Surface Pressure(kPa)')
plt.xlabel('Dates')
plt.title('Surface Pressure from 12/1/2019 to 6/1/2020')
lenap = len(avgpresarr)
plt.xticks(numpy.arange(1, lenap+1, 30)) #Not all dates are written on the x-axis

plt.show()
print('End Code')