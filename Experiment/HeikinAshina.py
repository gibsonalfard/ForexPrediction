

import pandas as pd


df = pd.read_csv('../Resources/EURJPY_traincopy.csv')



def heikin_ashi(df):
    heikin_ashi_df = pd.DataFrame(index=df.index.values, columns=['<OPEN>', '<HIGH>', '<LOW>', '<CLOSE>'])
    
    heikin_ashi_df['<CLOSE>'] = (df['<OPEN>'] + df['<HIGH>'] + df['<LOW>'] + df['<CLOSE>']) / 4
    
    for i in range(len(df)):
        if i == 0:
            heikin_ashi_df.iat[0, 0] = df['<OPEN>'].iloc[0]
        else:
            heikin_ashi_df.iat[i, 0] = (heikin_ashi_df.iat[i-1, 0] + heikin_ashi_df.iat[i-1, 3]) / 2
        
    heikin_ashi_df['<HIGH>'] = heikin_ashi_df.loc[:, ['<OPEN>', '<CLOSE>']].join(df['<HIGH>']).max(axis=1)
    
    heikin_ashi_df['<LOW>'] = heikin_ashi_df.loc[:, ['<OPEN>', '<CLOSE>']].join(df['<LOW>']).min(axis=1)
    
    return heikin_ashi_df
    


df['HeikinAshi'] = heikin_ashi(df)
df.plot(y=['HeikinAshi'])