

import pandas as pd


df = pd.read_csv('D:\Kuliah\Semester 4\Proyek 2 Data Scientific\EURJPY_train-2000-lines.csv')



heikin_ashi_df = pd.DataFrame(index=df.index.values, columns=['<OPEN>', '<HIGH>', '<LOW>', '<CLOSE>'])

heikin_ashi_df['<CLOSE>'] = (df['<OPEN>'] + df['<HIGH>'] + df['<LOW>'] + df['<CLOSE>']) / 4

#heikin_ashi_df['<OPEN>'] = (heikin_ashi_df['<OPEN>'].shift() + heikin_ashi_df['<CLOSE>'].shift()) / 2
for i in range(len(df)):
    if i == 0:
        heikin_ashi_df.loc[i, '<OPEN>'] = df.loc[i, '<OPEN>']
    else:
        heikin_ashi_df.loc[i, '<OPEN>'] = (heikin_ashi_df.loc[i-1, '<OPEN>'] + heikin_ashi_df.loc[i-1, '<CLOSE>']) / 2
#        heikin_ashi_df.iat[i, 0] = (heikin_ashi_df.iat[i-1, 0] + heikin_ashi_df.iat[i-1, 3]) / 2
    
heikin_ashi_df['<HIGH>'] = heikin_ashi_df.loc[:, ['<OPEN>', '<CLOSE>']].join(df['<HIGH>']).max(axis=1)

heikin_ashi_df['<LOW>'] = heikin_ashi_df.loc[:, ['<OPEN>', '<CLOSE>']].join(df['<LOW>']).min(axis=1)

for x in range(0, len(heikin_ashi_df)):
    if((heikin_ashi_df.loc[x, '<OPEN>'] == heikin_ashi_df.loc[x, '<LOW>']) or (heikin_ashi_df.loc[x, '<OPEN>'] == heikin_ashi_df.loc[x, '<HIGH>'])):
        print("Hello World")
        if(heikin_ashi_df.loc[x, '<OPEN>'] > heikin_ashi_df.loc[x, '<CLOSE>']):
            if(((heikin_ashi_df.loc[x, '<OPEN>'] - heikin_ashi_df.loc[x, '<CLOSE>']) - (heikin_ashi_df.loc[x, '<CLOSE>'] - heikin_ashi_df.loc[x, '<LOW>'])) > 0):
                df.loc[x, 'Signal HA'] = -1
            else:
                df.loc[x, 'Signal HA'] = 0
        elif((heikin_ashi_df.loc[x, '<CLOSE>'] - heikin_ashi_df.loc[x, '<OPEN>']) - (heikin_ashi_df.loc[x, '<HIGH>'] - heikin_ashi_df.loc[x, '<CLOSE>']) > 0):
            df.loc[x, 'Signal HA'] = 1
        else:
            df.loc[x, 'Signal HA'] = 0
    else:
        df.loc[x, 'Signal HA'] = 0

df.to_csv(r'D:\Kuliah\Semester 4\Proyek 2 Data Scientific\EURJPY_out_from_indicator_HA.csv', index = None, header=True)
#if((heikin_ashi_df['<OPEN>'].equals(heikin_ashi_df['<LOW>'])) or (heikin_ashi_df['<OPEN>'].equals(heikin_ashi_df['<HIGH>']))):
##    print("saasD")
#    if(heikin_ashi_df['<OPEN>'] > heikin_ashi_df['<CLOSE>']):
#        if(((heikin_ashi_df['<OPEN>'] - heikin_ashi_df['<CLOSE>']) - (heikin_ashi_df['<CLOSE>'] - heikin_ashi_df['<LOW>'])) > 0):
#            df['Signal'] = -1
#    elif((heikin_ashi_df['<CLOSE>'] - heikin_ashi_df['<OPEN>']) - (heikin_ashi_df['<OPEN>'] - heikin_ashi_df['<HIGH>']) > 0):
#        df['Signal'] = 1
#else:
#    df['Signal'] = 0