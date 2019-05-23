# -*- coding: utf-8 -*-
"""
Created on Thu May 16 10:13:18 2019

@author: Muhammad Reyhan S
"""

import pandas as pd
import numpy as np
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')

stocks = ['EURJPY']

df = pd.read_csv(r'D:\Kuliah\Semester 4\Proyek 2 Data Scientific\USDJPY_train-2000-lines.csv')

def RSI(series, period):
     delta = series.diff().dropna()
     u = delta * 0
     d = u.copy()
     u[delta > 0] = delta[delta > 0]
     d[delta < 0] = -delta[delta < 0]
     u[u.index[period-1]] = np.mean( u[:period] ) #first value is sum of avg gains
     u = u.drop(u.index[:(period-1)])
     d[d.index[period-1]] = np.mean( d[:period] ) #first value is sum of avg losses
     d = d.drop(d.index[:(period-1)])
     rs = pd.Series.ewm(u, com=period-1, adjust=False).mean() / \
     pd.Series.ewm(d, com=period-1, adjust=False).mean()
     return 100 - 100 / (1 + rs)
 
#Menentukan Buy and Sell
df['RSI'] = RSI(df['<CLOSE>'], 14)
arr_rsi = []
arr_rsi = df['RSI']
i=14
ind=[]
for x in range(0, 14):
    ind.append(float('NaN'))
for x in range(14, len(arr_rsi)):
    if((arr_rsi[i-1] >= 70) and (arr_rsi[i] < 70)):
        ind.append(-1)
    elif((arr_rsi[i-1] <= 30) and (arr_rsi[i] > 30)):
        ind.append(1)
    else:
        ind.append(0)
    i=i+1
#for x in range(14, len(arr_rsi)):
#    if(arr_rsi[i] >= 70):
#        ind.append(-1)
#    elif((arr_rsi[i] <= 30)):
#        ind.append(1)
#    else:
#        ind.append(0)
#    i=i+1

df['Signal RSI'] = ind
df.to_csv(r'D:\Kuliah\Semester 4\Proyek 2 Data Scientific\USDJPY_out_from_indicator_rsi.csv', index = None, header=True)
df.plot(y=['RSI'], title = 'RSI')
#df.tail()