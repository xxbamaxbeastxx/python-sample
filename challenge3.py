# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 22:28:55 2018

@author: shark
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as mplot
from PIL import Image



images=[]

count = 0
while count < 196:
    if count == 5 or count == 12 or count == 21 or count == 67 or count == 129 or count == 130 or count == 141 or count == 143 or count == 148 or count == 154:
        count+=1
        continue
    else:
        pic = "chall3pics\einsteinatanderson_" + str(count) + ".jpg"
        img=Image.open(pic)
        img=np.float32(img)
        images.append(img)
        count += 1
avgImg = images[0]

for x in range(1, len(images)):
    avgImg+=images[x]

avgImg/=len(images)

#avgCop = avgImg
temp = (images[0] - avgImg)
images[0] = temp ** 2
tot = images[0]
for x in range(1, len(images)):#calculates standard deviation image
    temp = (images[x] - avgImg)
    images[x] = temp ** 2
    tot += images[x]
dev = tot / len(images)
dev = np.sqrt(dev)
"""stanImg = []
for x in range(0, len(images)):
    stanImg.append(images[x])


for x in range(0, len(stanImg)):
    temp = stanImg[x]
    temp -= avgCop
    temp = (temp*temp)#np.power(temp, 2)
    stanImg[x] = temp

tot = stanImg[0]
for num in range(1, len(stanImg)):
    tot += stanImg[num]
tot = tot/len(stanImg)
dev = np.sqrt(tot)

#dev = statistics.stdev(images)"""

choice = input("Enter a value between 0 and 255\n")#the minimum standard deviation to be used

if choice.isalpha():
    print ("Invalid input, default of 0 will be used\n")
    choice = 0


choice = int(choice)
if choice > 255 or choice < 0:
    print ("Invalid input, default of 0 will be used\n")
    choice = 0



for row in range(0, len(avgImg)):
    for col in range(0, len(avgImg[row])):
        if (dev[row][col] > [choice, choice, choice]).any():
            avgImg[row][col]=[255, 0, 0]


"""just need standard deviation"""
avgImg=np.clip(avgImg, 0, 255)
avgImg=np.uint8(avgImg)

dev=np.clip(dev, 0, 255)
dev=np.uint8(dev)

mplot.imshow(avgImg)
mplot.show()
mplot.imshow(dev)
mplot.show()