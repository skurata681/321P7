
import netCDF4 as nc
from pylab import *
import numpy
import os
import pandas as pd

directory = os.fsencode('C:/Users/manis/Documents/C321Project_Local/mwrret1liljclou/')
fn = 'C:/Users/manis/Documents/C321Project_Local/mwrret1liljclou/'
GoodData = [[]]
dates = []

cool = 0
for file in os.listdir(directory):
    # access each files data to this pt
    fn = 'C:/Users/manis/Documents/C321Project_Local/mwrret1liljclou/'
    filename = os.fsdecode(file)
    fn += filename
    ds = nc.Dataset(fn)
    time = ds['time'][:]
    lendata = len(time)
    varnames = []
    for a in ds.variables:
        varnames.append(a)


  #at this point we add the second for loop to grab all the data, which is yikes!
  #grab the data in arrays for each day
    lenrick = len(varnames)  # calculate averages for what we need
    varnames1 = varnames[4:lenrick-7]
    Ravgdata = []
    date = filename[26:32]
    dates.append(int(date))
    Ravgdata.append(int(date))
    for a in varnames1:
        rawdata = ds[a][:]
        avgdata = sum(rawdata) / lendata
        Ravgdata.append(avgdata)  #take the average per day, and smack it into its array

 #Now we need to add this list to a list of lists to get all the data!
    if (cool==0):
        varnames1.insert(0, 'dates')
        GoodData.append(varnames1)
    GoodData.append(Ravgdata)

 #dates - which is one value per file, collected in a dates array.

    cool = 1
    #Forloop end


GoodData.pop(0)
my_df = pd.DataFrame(GoodData)
my_df.to_csv('DailyData.csv', index=False, header=False)
# at this point in the code, we have arrays of the daily average from 12/1 - 6/1 for all the data, which is ~meh~
#from here, we have to narrow down to the variables we want & 4/5/2020 - 4/11/2020
# dateswanted =[]
#
# counter = [] #these will be the columns wanted in GoodData
# lenap = len(dates)
#
# for x in range(lenap):
#     if dates[x] >= 200323 and dates[x] <= 200501:
#         dateswanted.append(dates[x+1])
#         counter.append(x)
# #What variables do you want?
# varw = ['surface_pres']
# x = []
# blue = []
# for i in varnames1:
#     if (i == varw[0]):
#        for b in counter:
#             blue.append(GoodData[b][i])
#
# #gives you the data you want
# plt.plot(dateswanted, blue)
# plt.title(varw[0])
# plt.show()
print('End Code')