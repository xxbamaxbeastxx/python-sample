# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 11:21:50 2018

OcherCanary
Mar 20, 2018
Challenge5

@author: shark
"""

#look at correlation for data sets. if 0 its random
#plot linear regression for the 2 non zero paths
import matplotlib.pyplot as mplot
import numpy as np

file=open("chall5/OcherCanary.csv", "r") 
data=file.read()
data=data[:-1]
data=data.split("\n") #splits data by line

xscatter=[] #x axis list for scatter plot
yscatter=[] #y axis list for scatter plot
xvalues = []
yvalues = []
isGood = []
frequencies = []
correl = []

for line in data:
    line=line.split(",")
    if (float(line[1]) not in frequencies):
        frequencies.append(float(line[1]))
for freq in frequencies:
    for line in data:#runs for all lines, last line has 1 space and 
        line=line.split(",") #gets columns from line
        secs = float(line[0])
        intensity = float(line[2])
        if (float(line[1]) == freq):#determine a way to store the frequency data
            xscatter.append(secs) #adds element 1 to xscatter
            yscatter.append(intensity)
    core = np.corrcoef(xscatter, yscatter)
    core = np.abs(core[0][1])
    correl.append(core)
    xvalues.append(xscatter)
    yvalues.append(yscatter)
    xscatter = []
    yscatter = []
one = 0
two = 0

for num in correl:#takes the top 2 cores
    if num > one:
        two = one
        one = num
    else:
        if num > two:
            two = num

for num in correl:
    if num == one or num == two:
        isGood.append(True)
    else:
        isGood.append(False)


mplot.title("Challenge 5")
mplot.xlabel("Milliseconds")
mplot.ylabel("Intensity")
mplot.scatter(xvalues[0], yvalues[0], color="orange", marker="o")
mplot.scatter(xvalues[1], yvalues[1], color="purple", marker="o")
mplot.scatter(xvalues[2], yvalues[2], color="black", marker="o")
mplot.scatter(xvalues[3], yvalues[3], color="yellow", marker="o")
mplot.scatter(xvalues[4], yvalues[4], color="green", marker="o")


for i in range(0, len(isGood)):
    if isGood[i] == True:#get poly fit and linear regression
        
        x = xvalues[i]
        y = yvalues[i]
        xy = []
        
        for k in range(0,len(xvalues[i])):
            xy.append([x[k],y[k]])
        value = xy
        value = sorted(value, key=lambda k: [k[0], k[1]])
        sortx, sorty = zip(*value)
        
        
        slope = np.corrcoef(x, y)[0][1] * (np.std(y)/np.std(x))
        b = np.mean(y) - (slope*np.mean(x))
        mplot.plot(x, x * np.array(slope) + b, color="red", linestyle="solid")#Wont accept slope as float
        
        if correl[i] == one:
            degree = 1
            para = np.polyfit(x, y, degree)
            predict = np.polyval(para, x)
            mplot.plot(x, predict, color="blue", linestyle="solid")
        if correl[i] == two:
            degree = 2
            para = np.polyfit(sortx, sorty, degree)
            predict = np.polyval(para, sortx)
            mplot.plot(sortx, predict, color="blue", linestyle="solid")
              
#print (xvalues[2])#1 and 3 are special
#mplot.plot(xvalues[1], poly[1], color="blue", linestyle="solid")
#mplot.plot(xvalues[3], xvalues[3] * 0.5 - linB[1], color="red", linestyle="solid")
mplot.show()
