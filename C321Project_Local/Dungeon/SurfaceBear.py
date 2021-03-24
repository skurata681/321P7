import matplotlib as plt
import netCDF4 as nc
from pylab import *
import numpy
import os

directory = os.fsencode('C:/Users/manis/Documents/C321p7DataManagement/SurfaceBear/')
fn = 'C:/Users/manis/Documents/C321p7DataManagement/SurfaceBear/'
avgpresarr = []
dates = []
for file in os.listdir(directory):
    fn = 'C:/Users/manis/Documents/C321p7DataManagement/SurfaceBear/'
    filename = os.fsdecode(file)
    fn += filename
    ds = nc.Dataset(fn)
    a = 'wxt_precip_rate_mean'
    surfpres = ds[a][:] #getting data
    lendata = len(surfpres)
    avgpres = sum(surfpres) / lendata #calculating avgerage pressure of the day
    avgpresarr.append(avgpres)
    date = filename[15:23]
    #date = date[2]+date[3]+"/"+date[4]+date[5] + "/" + date[0]+ date[1] #formatting date in standard format
    dates.append(date)
#print(avgpresarr)
#print(filename[26:32])

plt.figure()
plt.plot(dates, avgpresarr)
plt.ylabel(a)
plt.xlabel('Time')
#plt.title('Teamperature from 12/1/2019 to 6/1/2020')
lenap = len(avgpresarr)
plt.xticks(numpy.arange(1, lenap+1, 30)) #Not all dates are written on the x-axis

plt.show()
plt.figure()
dateswanted = []
Blue = []
count = -1
for i in dates:
    count += 1
    if (int(i)>20200301 and int(i)<20200431):
        dateswanted.append(i)
        Blue.append(avgpresarr[count])

plt.plot(dateswanted, Blue)
plt.ylabel(a)
plt.xlabel('Time')
r = len(Blue)
plt.xticks(numpy.arange(1, r+1, 10))
print('End Code')