"""
Last updated Fri 6/23/2023 16:14:45

@author: catherine
"""

import sys
sys.modules[__name__].__dict__.clear()
import matplotlib
from matplotlib import pyplot as plt
import pandas as pd
import math

def resetVar():
    global wavelength
    global intensity_1 # sample 1
    global intensity_2 # sample 2
    global intensity_3 # sample 3
    global mean_all # calculated mean from 3 samples at each wavelength
    global std_all # calculated std from 3 samples at each wavelength
    global Plus # mean + std
    global Minus # mean - std

    wavelength = []
    intensity_1 = []
    intensity_2 = []
    intensity_3 = []
    mean_all = []
    std_all = []
    Plus = []
    Minus = []

def readFile(file1,file2,file3):
    with open(file1) as file_1:
        lines_1 = file_1.readlines()

    with open(file2) as file_2:
        lines_2 = file_2.readlines()

    with open(file3) as file_3:
        lines_3 = file_3.readlines()

    wavelengthSplit(lines_1,wavelength)
    intensitySplit(lines_1,intensity_1)
    intensitySplit(lines_2,intensity_2)
    intensitySplit(lines_3,intensity_3)

def wavelengthSplit(Lines,wv):
    for line in Lines:
        if "," in line and "\"" not in line:
            #res = any(chr.isdigit() for chr in line)
            #if res == True:
                #print(line, end='')
            for word in line.split(","):
                if "." not in word:
                    word = int(word)
                    wv.append(word)

def intensitySplit(Lines,intensity_values):
    for line in Lines:
        if "," in line and "\"" not in line:
            #res = any(chr.isdigit() for chr in line)
            #if res == True:
                #print(line, end='')
            for word in line.split(","):
                if "." in word:
                    word = float(word)
                    intensity_values.append(word)

def stats(list1,list2,list3):
    for i in range(len(list1)):
        value_1 = list1[i]
        value_2 = list2[i]
        value_3 = list3[i]
        mean = ( value_1 + value_2 + value_3 ) / 3
        mean_all.append(mean)
        std = math.sqrt( ((value_1 - mean)**2 + (value_2 - mean)**2 + (value_3 - mean)**2)/2)
        std_all.append(std)
    print(wavelength[296],mean_all[296])

def graph(colour,name):
    for i in range(len(intensity_1)):
        plus = mean_all[i] + std_all[i]
        minus = mean_all[i] - std_all[i]
        Plus.append(plus)
        Minus.append(minus)

    plt.plot(wavelength,mean_all,alpha=1,color=colour,label=name)
    plt.plot(wavelength,Plus,alpha=0.2,color=colour)
    plt.plot(wavelength,Minus,alpha=0.2,color=colour)
    plt.fill_between(wavelength, Minus,Plus,color=colour,alpha = 0.2)

    plt.legend()

plt.style.use('default')
plt.figure(dpi=100)
hfont = {'fontname':'Arial'}
plt.xlim(200,800)
#plt.ylim(4, 4.5)
plt.ylabel('Intensity (a.u.)', fontsize = 18, **hfont)
plt.xlabel("Wavelength (nm)", fontsize = 18, **hfont)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# 6.4
resetVar()
readFile('6.4_1.txt','6.4_2.txt','6.4_3.txt')
stats(intensity_1,intensity_2,intensity_3)
print('6.4',pd.Series(mean_all).idxmax())
graph('cyan','6.4 ng/mL')


# 32
resetVar()
readFile('32_1.txt','32_2.txt','32_3.txt')
stats(intensity_1,intensity_2,intensity_3)
print('32',pd.Series(mean_all).idxmax())
graph('fuchsia','32 ng/mL')

# 160
resetVar()
readFile('160_1.txt','160_2.txt','160_3.txt')
stats(intensity_1,intensity_2,intensity_3)
print('160',pd.Series(mean_all).idxmax())
graph('crimson','160 ng/mL')

# 800
resetVar()
readFile('800_1.txt','800_2.txt','800_3.txt')
stats(intensity_1,intensity_2,intensity_3)
print('800',pd.Series(mean_all).idxmax())
graph('indigo','800 ng/mL')

# 4000
resetVar()
readFile('4000_1.txt','4000_2.txt','4000_3.txt')
stats(intensity_1,intensity_2,intensity_3)
print('4000',pd.Series(mean_all).idxmax())
graph('green','4000 ng/mL')

#figure 2
plt.style.use('default')
plt.figure(dpi=100)
hfont = {'fontname':'Arial'}
plt.xlim(200,800)
plt.ylim(0, 600)
plt.ylabel('Intensity (a.u.)', fontsize = 18, **hfont)
plt.xlabel("Wavelength (nm)", fontsize = 18, **hfont)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# HDM
resetVar()
readFile('hdm_1.txt','hdm_2.txt','hdm_3.txt')
stats(intensity_1,intensity_2,intensity_3)
print('HDM',pd.Series(mean_all).idxmax())
graph('orange','HDM')


# blank
resetVar()
readFile('blank_1.txt','blank_2.txt','blank_3.txt')
stats(intensity_1,intensity_2,intensity_3)
print('Blank',pd.Series(mean_all).idxmax())
graph('blue','Blank')

plt.show()