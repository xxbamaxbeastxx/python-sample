# -*- coding: utf-8 -*-
"""
OcherCanary
Last edit 2/9/2018
challenge 1

@author: shark
"""


import matplotlib.pyplot as mplot


file=open("OcherCanary_ch1.csv", "r") 
data=file.read()
data=data[:-1]
data=data.split("\n") #splits data by line

xscatter=[] #x axis list for scatter plot
yscatter=[] #y axis list for scatter plot
xline=[]
yline=[]
count = 0

for line in data:#runs for all lines, last line has 1 space and 
    
    line=line.split(",") #gets columns from line
    secs = float(line[0])
    amp = float(line[1])
    if (float(line[2]) == 58.471186):  #  20.358852
        #count += 1
        freq = float(line[2])
        xscatter.append(secs) #adds element 1 to xscatter
        yscatter.append(amp)
    """if (count == 20):
        xline.append(x/20)
        yline.append(y/20)
        count = 0
        x = 0
        y = 0"""
mean=[]
count = 0
tot = 0
"""unique = list(set(xscatter))
unique = sorted(unique)"""
unique=[]
current = xscatter[0]
unique.append(current)
for x in range(0, len(xscatter)):
    if (current != xscatter[x]):
        unique.append(current)
        current = xscatter[x]
for x in range(0, len(unique)):
    for y in range(0, len(xscatter)):
        if (unique[x] == xscatter[y]):
            tot += yscatter[y]
            count += 1       
    avg = tot/count
    mean.append(avg)
    tot = 0
    count = 0
mplot.title("")
mplot.xlabel("Milliseconds")
mplot.ylabel("Amp")
#generates scatter plot

mplot.scatter(xscatter, yscatter, color="red", marker="o")
#generates line plot
mplot.plot(unique, mean, color="blue", linestyle="solid")
#displays the plot
mplot.show()