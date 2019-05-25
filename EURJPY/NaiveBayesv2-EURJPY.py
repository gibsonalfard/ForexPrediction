# -*- coding: utf-8 -*-

#   Created on Wed Apr 17 06:05:29 2019

#   @author: Ilham Gibran


#To find similarity between two number
import math
import pandas as pd

def countPercent(data):
	return (data[0]/data[4])*(data[1]/data[4])*(data[2]/data[4])*(data[3]/data[4])

def similarityNumber(num1, num2):
    maxi = num1 if num1>num2 else num2
    mini = num2 if maxi == num1 else num1

    return (mini ** 2)/math.sqrt(maxi**2 * mini**2)

def checker(dataset, test, kelas):
    if (similarityNumber(dataset[0], test[0])>0.99):
        kelas[0] += 1
    if (similarityNumber(dataset[1], test[1])>0.99):
        kelas[1] += 1
    if (similarityNumber(dataset[2], test[2])>0.99):
        kelas[2] += 1;
    if (similarityNumber(dataset[3], test[3])>0.99):
        kelas[3] += 1;
    
def whichClass(buyPercent, sellPercent, holdPercent):
    action = ""
    if buyPercent > sellPercent:
        if buyPercent > holdPercent :
            action = "Buy"
        else:
            action = "Hold"
    else:
        if sellPercent > holdPercent :
            action = "Sell"
        else:
            action = "Hold"
    return action
        
# Importing the training set
dataset_train = pd.read_csv('../Resources/EURJPY_out_all_signal.csv')
#training_set_open = dataset_train.iloc[:, 3:4].values
#training_set_high = dataset_train.iloc[:, 4:5].values
#training_set_low = dataset_train.iloc[:, 5:6].values
#training_set_close = dataset_train.iloc[:, 6:7].values
#training_set_ha = dataset_train.iloc[:, 8:9].values
training_set_ = dataset_train.iloc[:, 3:9].values

# Get New Data
newData = dataset_train.iloc[:, 3:7].values

#buy = [0,0,0,0,0]
#sell = [0,0,0,0,0]
#hold = [0,0,0,0,0]
for j in range (0, newData.shape[0]):
    signalValue = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    for i in range(0, training_set_.shape[0]-1):
        if (training_set_[i, 5] == 1):
            signalValue[0][4] += 1;
            checker(training_set_[i, :],newData[j],signalValue[0])
        elif (training_set_[i, 5] == -1):
            signalValue[1][4] += 1;
            checker(training_set_[i, :],newData[j],signalValue[1])
        else:
            signalValue[2][4] += 1;
            checker(training_set_[i, :],newData[j],signalValue[2])
    print(countPercent(signalValue[0]), " - ",countPercent(signalValue[1]), " - ", countPercent(signalValue[2]))
    print("Menurut Heiken Ashi FOREX ini harus di", whichClass(countPercent(signalValue[0]), countPercent(signalValue[1]), countPercent(signalValue[2])))