# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 06:40:07 2019

@author: Muhammad Reyhan S
"""

import pandas as pd
import numpy as np
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')

stocks = ['EURJPY']

df = pd.read_csv('D:\Kuliah\Semester 4\Proyek 2 Data Scientific\EURJPY_train-2000-lines.csv')
df['26 ema'] = pd.Series.ewm(df['<CLOSE>'], span=26, adjust=False).mean()
df['12 ema'] = pd.Series.ewm(df['<CLOSE>'], span=12, adjust=False).mean()
df['MACD'] = (df['12 ema'] - df['26 ema'])
df['Signal Line'] = pd.Series.ewm(df['MACD'], span=9, adjust=False).mean()
df['Signal Line Crossover'] = np.where(df['MACD'] > df['Signal Line'], 1, 0)
df['Signal Line Crossover'] = np.where(df['MACD'] < df['Signal Line'], -1, df['Signal Line Crossover'])
df['Centerline Crossover'] = np.where(df['MACD'] > 0, 1, 0)
df['Centerline Crossover'] = np.where(df['MACD'] < 0, -1, df['Centerline Crossover'])

arr_macd=[]
arr_s_line=[]
ind=[]
arr_macd = df['MACD']
arr_s_line = df['Signal Line']

i = 0
for x in range(0, len(arr_macd)):
    if(((arr_macd[i] > arr_s_line[i])) and (arr_macd[i-1] <= arr_s_line[i-1])):
        ind.append(1)
    elif(((arr_macd[i] < arr_s_line[i]))and (arr_macd[i-1] >= arr_s_line[i-1]) ):
        ind.append(-1)
    else:
        ind.append(0)
    i=i+1
    
df['Signal MACD'] = ind
#df['Buy Sell'] = (2*(np.sign(df['Signal Line Crossover'] - df['Signal Line Crossover'].shift(1))))
df.to_csv(r'D:\Kuliah\Semester 4\Proyek 2 Data Scientific\EURJPY_out_from_indicator_macd.csv', index = None, header=True)
df.plot(y=['<CLOSE>'], title='Close')
df.plot(y=['MACD', 'Signal Line'], title='MACD & Signal Line')
#df.plot(y=['Centerline Crossover', 'Buy Sell'], title='Signal Line & Centerline Crossover', ylim=(-3,3))