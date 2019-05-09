# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 07:17:57 2019

@author: Gibran
"""

import pandas as pd
import numpy as np
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')

def get_stock():
# return web.DataReader(stock,'google',start,end)['Close']
  return pd.read_csv('../Resources/EURUSD-Training.csv')
    
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
 rs = pd.DataFrame.ewm(u, com=period-1, adjust=False).mean() / \
 pd.DataFrame.ewm(d, com=period-1, adjust=False).mean()

 value = 100 - (100 / (1 + rs.iloc[0]))
 print(value)

 return value

df = pd.DataFrame(get_stock())
#bk = df;
for i in range(1, len(df)):
   df.loc[i-1,'RSI'] = RSI(df['Open'], i)
   print(i)
df.to_csv(path_or_buf="../Resources/BackUp.csv")
df.tail()

plt.plot(df["Open"], color="green", label = "Real Data")
plt.show