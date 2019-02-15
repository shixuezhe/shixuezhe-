#_*_ coding:utf-8 _*_

import pandas as pd
import numpy as np
def co2():
    df_climate=pd.read_excel("ClimateChange.xlsx", sheetname='Data')
    data=df_climate[df_climate['Series code'] == 'EN.ATM.CO2E.KT'].set_index('Country code')
    data=data.drop(['Country name','Series code','Series name','SCALE','Decimals'],axis=1)
    data=data.replace({'..':pd.np.nan})
    data=data.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    data_sum=data.sum(axis=1)
    
    df_country=pd.read_excel("ClimateChange.xlsx", sheetname='Country')
    df_country.index=df_country['Country code']
    country=df_country['Income group']

    df_sum=pd.concat([data_sum,country],axis=1)
    df_sum_data=df_sum.groupby('Income group').sum()
    df_sum_data.columns=['Sum emissions']

    df_sum['new']=df_country['Country name']
    df_sum=df_sum.reindex(columns=['new',0,'Income group'])
    df_sum=df_sum.dropna()
    highest=df_sum.sort_values(0,ascending=False).groupby('Income group').head(1).set_index('Income group')
    highest.columns=['Highest emission country','Highest emissions']

    lowest=df_sum.sort_values(0).groupby('Income group').head(1).set_index('Income group')
    lowest.columns=['Lowest emission country','Lowest emissions']

    results=pd.concat([df_sum_data,highest,lowest],axis=1)
    return results

if __name__=='__main__':
    co2()
