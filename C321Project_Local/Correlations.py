from pylab import *
import numpy
import os
import pandas as pd

AvgData = pd.read_csv("DailyData.csv")
# Use `iloc[]` to select row `0`
green = list(AvgData)


dates = list(AvgData.loc[:, 'dates'])
dateswanted = []
startdate = 200323
enddate = 200423
instart = dates.index(startdate) #index's  to cut variable data
inend = dates.index(enddate)
for i in dates:
    if (i>=startdate and i <=enddate):
        blue = str(i)
        dateswanted.append(blue[2]+blue[3]+"/"+blue[4]+blue[5] + "/" + blue[0]+ blue[1])
corr = []
for i in range(0, 72):
    if (i!=0):
        col1 = AvgData["surface_pres"][instart:inend + 1]
        col2 = pd.to_numeric(AvgData.iloc[:, i][instart:inend + 1])
        corr.append(abs(col1.corr(col2)))
corrvar = []
for i in range(0, len(corr)):
    if (corr[i]>0.35):
        corrvar.append(green[i+1])

# What variables do you you want?
varnames = corrvar #add as many as you need, the for loop plots it
for i in varnames:
    y = list(AvgData.loc[:, i])
    y = y[instart:inend+1]
    plt.figure()
    plt.plot(dateswanted, y)
    plt.xlabel('Dates')
    plt.ylabel(i)
    plt.xticks(numpy.arange(0, inend-instart +1, 10))
    plt.show()

