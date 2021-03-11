from pylab import *
import numpy
import os
import pandas as pd

AvgData = pd.read_csv("DailyData.csv")
# Use `iloc[]` to select row `0`



dates = list(AvgData.loc[:, 'dates'])
dateswanted = []
instart = dates.index(200323)
inend = dates.index(200423)
for i in dates:
    if (i>=200323 and i <=200423):
        blue = str(i)
        dateswanted.append(blue[2]+blue[3]+"/"+blue[4]+blue[5] + "/" + blue[0]+ blue[1])
# for i in range(0,len(dates)):
#     dateswanted[i] = str(dateswanted[i])
#     dates[i] = dates[i][2]+dates[i][3]+"/"+dates[i][4]+dates[i][5] + "/" + dates[i][0]+ dates[i][1]

# What variables do you want?
varnames = ['surface_pres', 'surface_temp', ]
for i in varnames:
    y = list(AvgData.loc[:, i])
    y = y[instart:inend+1]
    plt.figure()
    plt.plot(dateswanted, y)
    plt.xlabel('Dates')
    plt.ylabel(i)
    plt.xticks(numpy.arange(0, inend-instart +1, 10))
    plt.show()

