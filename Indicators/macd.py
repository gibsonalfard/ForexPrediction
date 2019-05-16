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

df = pd.read_csv('D:\Kuliah\Semester 4\Proyek 2 Data Scientific\EURJPY_traincopy.csv')
df['26 ema'] = pd.Series.ewm(df['<CLOSE>'], span=26, adjust=False).mean()
df['12 ema'] = pd.Series.ewm(df['<CLOSE>'], span=12, adjust=False).mean()
df['MACD'] = (df['12 ema'] - df['26 ema'])
df['Signal Line'] = pd.Series.ewm(df['MACD'], span=9, adjust=False).mean()
df['Signal Line Crossover'] = np.where(df['MACD'] > df['Signal Line'], 1, 0)
df['Signal Line Crossover'] = np.where(df['MACD'] < df['Signal Line'], -1, df['Signal Line Crossover'])
df['Centerline Crossover'] = np.where(df['MACD'] > 0, 1, 0)
df['Centerline Crossover'] = np.where(df['MACD'] < 0, -1, df['Centerline Crossover'])
df['Buy Sell'] = (2*(np.sign(df['Signal Line Crossover'] - df['Signal Line Crossover'].shift(1))))

df.plot(y=['<CLOSE>'], title='Close')
df.plot(y=['MACD', 'Signal Line'], title='MACD & Signal Line')
df.plot(y=['Centerline Crossover', 'Buy Sell'], title='Signal Line & Centerline Crossover', ylim=(-3,3))