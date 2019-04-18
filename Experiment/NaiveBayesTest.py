# -*- coding: utf-8 -*-

#   Created on Wed Apr 17 06:05:29 2019

#   @author: Ilham Gibran


#To find similarity between two number
import math
import pandas as pd

def countPercent(data):
	return (data[0]/data[3])*(data[1]/data[3])*(data[2]/data[3])

def similarityNumber(num1, num2):
    maxi = num1 if num1>num2 else num2
    mini = num2 if maxi == num1 else num1

    return (mini ** 2)/math.sqrt(maxi**2 * mini**2)

def checker(harga, pajak, seat, test, kelas):
    if (similarityNumber(harga, test[0])>0.65):
        kelas[0] += 1
    if (similarityNumber(pajak, test[1])>0.65):
        kelas[1] += 1
    if (similarityNumber(seat, test[2])>0.65):
        kelas[2] += 1;
    
def whichClass(var1, var2):
    return "Mewah" if var1 > var2 else "Biasa"
        
# Importing the training set
dataset_train = pd.read_csv('../Resources/TrainNaive.csv')
training_set_harga = dataset_train.iloc[:, 0:1].values
training_set_pajak = dataset_train.iloc[:, 1:2].values
training_set_seat = dataset_train.iloc[:, 2:3].values
training_set_class = dataset_train.iloc[:, 3:4].values

# Get New Data
newData = [200, 4.5, 2]

luxury = [0,0,0,0]
normal = [0,0,0,0]

for i in range(0, len(training_set_harga)):
    if (training_set_class[i,0] == "Lux"):
        luxury[3] += 1;
        checker(training_set_harga[i,0],training_set_pajak[i,0],training_set_seat[i,0],newData,luxury)
    else:
        normal[3] += 1;
        checker(training_set_harga[i,0],training_set_pajak[i,0],training_set_seat[i,0],newData,normal)

print("Mobil Ini Tergolong", whichClass(countPercent(luxury), countPercent(normal)))