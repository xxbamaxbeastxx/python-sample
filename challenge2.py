# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 11:49:31 2018

@author: shark
"""
#useful for challeng2
import numpy as np
import matplotlib.pyplot as mplot
import glob

series='A'
file=open("sentiment_lex_header.csv", "r") 
header=file.read()
header=header[:-1]
header=header.split("\n") #splits data by line

file=open("sentiment_lex.csv", "r") 
data=file.read()
data=data[:-2]
data=data.split("\n") #splits data by line

values = {}

for line in data:
    line = line.split(",")
    values[line[0]] = line[1]

tex = glob.glob("text2/*.txt")

readA =[]
readB =[]
count = 0
file = open(tex[count])
f = file.read()
f = f.split(" ")

for x in tex:
    file = open(tex[count])
    if (count < 22):
        readA.append(file.read())
        readA[count] = readA[count].split(" ")
    if (count >= 22):
        readB.append(file.read())
        readB[count-22] = readB[count-22].split(" ")
    count+=1

aCharacters = []
for x in readA:
    for word in x:
        if not word.isalpha():
            continue
    
        if len(word) == 1:
            continue#stops the loop skips the value and moves on
    
        if word==word.upper() and len(word)>1:
            aCharacters.append(word)
aCharacters=list(set(aCharacters))
a_ct={}
for x in readA:
    for word in x:
        if word in aCharacters:
            try:
                a_ct[word] +=1
            except:
                a_ct[word]=1
aWords = []
for x in readA:
    for word in x:
        if not word.isalpha():
            continue
        if len(word) == 1:
            continue
        if not word == word.upper() and len(word)>1:
            aWords.append(word.lower())
#aWords = list(set(aWords))
aSent = {}

bWords = []
for x in readB:
    for word in x:
        if not word.isalpha():
            continue
        if len(word) == 1:
            continue
        if not word == word.upper() and len(word)>1:
            bWords.append(word.lower())
#aWords = list(set(aWords))
bSent = {}


aNeg = 0
aWNeg = 0
aNeu = 0
aWPos = 0
aPos=0

count = 0
for word in aWords:#compare the words in aWords to the words in sentiment value and get the value
    if word in values:
        count+=1
        temp = float(values.get(word));
        if temp > 0.6:
             aPos+=1;
        if temp > 0.2 and temp <= 0.6:
            aWPos+=1;
        if temp >= -0.2 and temp <= 0.2:
            aNeu += 1;
        if temp >= -0.6 and temp < -0.2:
            aWNeg+=1;
        if temp >= -1.0 and temp < -0.6:
            aNeg += 1;
sent=[aNeg, aWNeg, aNeu, aWPos, aPos]
x = [-2.0, -1.0, 0.0, 1.0, 2.0]

bNeg = 0
bWNeg = 0
bNeu = 0
bWPos = 0
bPos=0


    
count = 0
for word in bWords:#compare the words in aWords to the words in sentiment value and get the value
    if word in values:
        count+=1
        temp = float(values.get(word));
        if temp > 0.6:
             bPos+=1;
        if temp > 0.2 and temp <= 0.6:
            bWPos+=1;
        if temp >= -0.2 and temp <= 0.2:
            bNeu += 1;
        if temp >= -0.6 and temp < -0.2:
            bWNeg+=1;
        if temp >= -1.0 and temp < -0.6:
            bNeg += 1;


choice = input("Enter 1 for Andromeda or 2 for Battlestar Galactica!\n")
"""while choice != 'A' or choice != 'B':
    print ("invalid input!")
    choice = input("Enter A for Andromeda or B for Battlestar Galactica!\n")"""

series="Andromeda"



if choice == "2":
    series="Battlestar"
    sent=[bNeg, bWNeg, bNeu, bWPos, bPos]
    x = [-2.0, -1.0, 0.0, 1.0, 2.0]

"""bCharacters = []
for x in readB:
    for word in x:
        if not word.isalpha():
            continue
    
        if len(word) == 1:
            continue#stops the loop skips the value and moves on
    
        if word==word.upper() and len(word)>1:
            bCharacters.append(word)

bCharacters=list(set(bCharacters))

b_ct={}

for x in readB:
    for word in x:
        if word in bCharacters:
            try:
                b_ct[word] +=1
            except:
                b_ct[word]=1
"""


#add in option to choose a or b and copy implementation of A

y=np.log10(sent)
mplot.title("Sentiment Analysis for Series " + series)
#draws bar plot
mplot.bar(x, y)
#sets x tick labels
mplot.xticks(x, ["Neg", "W.Neg", "Neu", "W.Pos", "Pos"])
#sets x axis label
mplot.xlabel("Sentiment")
#sets y axis label
mplot.ylabel("log10 Word Count")
#displays plot
mplot.show()
