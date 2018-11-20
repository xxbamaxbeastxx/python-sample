# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 11:17:38 2018

OcherCanary
Mar 29, 2018
Challenge4

@author: shark
"""
import matplotlib.pyplot as mplot
import numpy as np
import time
import math
import random

def ran(k):
    return random.randint(0, k)

def dist(a, b):
    return math.sqrt(math.pow(a[0]-b[0],2)+math.pow(a[1]-b[1],2))
def findKnn(data, k):
    grid = []
    reconstructed = []
    nearest = []
    v = 0
    dis = 0
    for x in range(0, 194):
        for y in range(0, 120):
            grid.append([x, y, v])
    for x in range(0, len(grid)):
        #for y in range(0, len(grid[0])):
        for i in range(0, len(data)):
            dis = dist([grid[x][0],grid[x][1]], [data[i][0], data[i][1]])
            #print([x, y])
            nearest.append([dis, data[i][2]])
        nearest = sorted(nearest, key=lambda val:val[0])
        value = 0
        for i in range(0, k):
            value += nearest[i][1]
        reconstructed.append([grid[x][0], grid[x][1], value])
        nearest = []
    return reconstructed


file=open("chall4/data.csv", "r") 
data=file.read()
data=data[:-1]
data=data.split("\n") #splits data by line"""

points = []
x = []
y = []
v = []

for line in data:
    line=line.split(",")
    points.append([float(line[0]), float(line[1]), float(line[2])])
    #x.append(float(line[0]))
    #y.append(float(line[1]))
    #v.append(float(line[2]))


file=open("chall4/us_outline.csv", "r") 
us=file.read()
us=us[:-1]
us=us.split("\n") #splits data by line
top = []
bottom = []
for n in us:
    n=n.split(",")
    top.append(float(n[0]))
    bottom.append(float(n[1]))

choice = int(input("Enter a k value\n"))
"""if choice.isalpha():
    print ("Invalid input, default of 1 will be used\n")
    choice = 1"""


final = findKnn(points, choice)
for i in final:
    x.append(i[0])
    y.append(i[1])
    v.append(i[2])
#x = horizontal grid pos
#y = vertical grid pos
#v = population change reconstructed

mplot.plot(top, bottom, color="black", linestyle="solid")
mplot.scatter(x, y, c=v, cmap="viridis")


mplot.show()

