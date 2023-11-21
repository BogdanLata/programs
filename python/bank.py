# -*- coding: utf-20 -*-
"""
Spyder Editor

This is a temporary script file
"""
import numpy as np
import pandas as pd 
import pickle, io
datadir = '/home/dan/Desktop/Unified small files/python/bankdata'

dfc1=pd.read_csv(f'{datadir}/feb22.csv',sep=',')
dfc2=pd.read_csv(f'{datadir}/apr26.csv',sep=';')
df1=pd.concat([dfc1,dfc2],ignore_index=True)
dfc2=pd.read_csv(f'{datadir}/july16.csv',sep=';')
dfc3=pd.read_csv(f'{datadir}/sept12.csv',sep=';')
dfc4=pd.read_csv(f'{datadir}/nov18.csv',sep=';')

df2 = dfc2[pd.to_datetime(dfc2['Trade date'],format='%d/%m/%Y')> 
           pd.to_datetime('26/04/2023',format='%d/%m/%Y')]
df3 = dfc3[pd.to_datetime(dfc3['Trade date'],format='%d/%m/%Y')>
           pd.to_datetime('14/07/2023',format='%d/%m/%Y')]
df4 = dfc4[pd.to_datetime(dfc4['Trade date'],format='%d/%m/%Y')>
           pd.to_datetime('11/09/2023',format='%d/%m/%Y')]

dfr=pd.concat([df1,df2,df3,df4],ignore_index=True)
dfr['Trade date'] = pd.to_datetime(dfr['Trade date'],format='%d/%m/%Y').dt.date
dfrx = dfr.sort_values(by='Trade date',ascending=True,ignore_index=True)


dn=dfrx.to_numpy()
l=[x for x in list(set(dn[:,6])) if not (x != x)]

# set makes them unique, x!=x excludes nan
counts=[];a=np.empty((0,2));
for i in l:
    count=0;sum=0;
    for row in dn:
        if row[6]==i :
         if row[8]=='Buy':
              count=count+row[9];sum=sum+row[12]
         if row[8]=='Sell': 
              count=count-row[9];sum=sum+row[12];
         if row[8]=='Dividend':sum=sum+row[12]
    if count!=0: if row[5]!='TSLA':
         print(i);print(count);print(sum)
    else:
                        if  row[5]=='USA': 
                               sum=sum*1.3508
                               a=np.vstack([a,[i,sum]])
                        else:  
                               a=np.vstack([a,[i,sum]])
a = [[row[0], row[1] + 731.5 * 1.3508] if row[0] == 'TSLA' else row for row in a]

a= np.array(a, dtype=object)
a[:,1]=a[:,1].astype(float);
sorteda = a[a[:, 1].argsort()]


f = dfrx[(dfrx.iloc[:, 6] == 'TSLA')]
        # & (dfrx.iloc[:, 8].isin(['Buy', 'Sell','Dividend']))]
af = a[a[:, 0] == 'IBM'];print(af[:,1])




#Use pickle to transfer dataframes to other scripts
fp = io.BytesIO()
pickle.dump(df3,fp)

#verifies if there is a symbol that appears in both USD and CAN
for i in l:
    notunique='False'
    f = dfrx[(dfrx.iloc[:, 6] == i) & (dfrx.iloc[:, 8].isin(['Buy','Sell']))]
    notunique=f['Market'].duplicated().any()
    if not notunique: print(i)
