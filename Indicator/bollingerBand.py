# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:07:48 2019

@author: Muhammad Reyhan S
"""

import pandas as pd
import numpy as np
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')

stocks = ['EURJPY']

df = pd.read_csv(r'D:\Kuliah\Semester 4\Proyek 2 Data Scientific\USDJPY_train-2000-lines.csv')

#pd.stats.moments.rolling_mean(df,20) #depecrated
#pd.stats.moments.rolling_std(df,20) #depecrated
df['20 ma'] = df['<CLOSE>'].rolling(window = 20).mean()
df['20 sd'] = df['<CLOSE>'].rolling(window = 20).std()
df['Upper Band'] = df['20 ma'] + (df['20 sd']*2)
df['Lower Band'] = df['20 ma'] - (df['20 sd']*2)
df.plot(y=['<CLOSE>','20 ma', 'Upper Band', 'Lower Band'], title='Bollinger Bands', figsize = (20, 5))