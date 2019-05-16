# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')

def STOK(close, low, high, nPeriod):
    STOK = ((close - low.rolling(nPeriod).min() / (high.rolling(nPeriod).max() - low.rolling(nPeriod).min()))) * 100
    return STOK

def STOD(close, low, high, nPeriod):
    STOK = ((close - low.rolling(nPeriod).min()) / (high.rolling(nPeriod).max() - low.rolling(nPeriod).min())) * 100
    STOD = STOK.rolling(3).mean()
    return STOD

df = pd.read_csv('D:\Kuliah\Semester 4\Proyek 2 Data Scientific\EURJPY_traincopy.csv')

array_high = df['<HIGH>']
array_low = df['<LOW>']
array_close = df['<CLOSE>']

y=0
z=0
# kperiods are 14 array start from 0 index
kperiods=13
array_highest=[]
for x in range(0,array_high.size-kperiods):
	z=array_high[y]
	for j in range(0,kperiods):
		if(z<array_high[y+1]):
			z=array_high[y+1]
		y=y+1
	# creating list highest of k periods
	array_highest.append(z)
  # skip one from starting after each iteration
	y=y-(kperiods-1)
    
y=0
z=0
array_lowest=[]
for x in range(0,array_low.size-kperiods):
	z=array_low[y]
	for j in range(0,kperiods):
		if(z>array_low[y+1]):
			z=array_low[y+1]
		y=y+1
	# creating list lowest of k periods
	array_lowest.append(z)
  # skip one from starting after each iteration
	y=y-(kperiods-1)

Kvalue=[]
for x in range(0,kperiods):
    Kvalue.append(float('NaN'))
    
for x in range(kperiods,array_close.size):
   k = ((array_close[x]-array_lowest[x-kperiods])*100/(array_highest[x-kperiods]-array_lowest[x-kperiods]))
   Kvalue.append(k)
   
df['%K'] = Kvalue

y=0
# dperiods for calculate d values
dperiods=3
Dvalue=[None,None]
mean=0
for x in range(0,len(Kvalue)-dperiods+1):
	sum=0
	for j in range(0,dperiods):
		sum=Kvalue[y]+sum
		y=y+1
	mean=sum/dperiods
	# d values for %d line adding in the list Dvalue
	Dvalue.append(mean)
  # skip one from starting after each iteration
	y=y-(dperiods-1)
    
df['%D'] = Dvalue

#Menentukan buy sell hold
i=15
ind=[]
for x in range(0, 15):
    ind.append(float('NaN'))

for x in range(15, len(Kvalue)):
    if(((Dvalue[i-1] < 20 and Kvalue[i-1] < 20) and (Kvalue[i] > Dvalue[i]))and (Kvalue[i-1] == Dvalue[i-1])):
        ind.append(1)
    elif(((Dvalue[i-1] > 80 and Kvalue[i-1] > 80) and (Kvalue[i] < Dvalue[i]))and (Kvalue[i-1] == Dvalue[i-1]) ):
        ind.append(-1)
    else:
        ind.append(0)
    i=i+1

#print(len(Kvalue))
df['ind'] = ind