#_*_ coding:utf-8 _*_
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def climate_plot():
    df_temperature = pd.read_excel("GlobalTemperature.xlsx")

    df_climate = pd.read_excel("ClimateChange.xlsx", sheetname='Data')

    data=df_climate[df_climate['Series code'].isin(['EN.ATM.CO2E.KT','EN.ATM.METH.KT.CE','EN.ATM.NOXE.KT.CE','EN.ATM.GHGO.KT.CE','EN.CLC.GHGR.MT.CE'])]     
    air_data=data.drop(data.columns[:6],axis=1)
    air_data=air_data.drop([2011],axis=1)
    air_data.replace({'..':pd.np.nan})
    air_data=air_data.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    air_sum=air_data.sum()
#    air_sum=air_sum.drop([2011])

    data1=df_temperature.drop(['Land Max Temperature','Land Min Temperature'],axis=1)
    i=pd.to_datetime(data1['Date'])
    data_1=pd.DataFrame(data=data1.values,columns=data1.columns,index=i)
    data_1=data_1.dropna(thresh=2)
    data_1=data_1.fillna(value=0)
    data_2=data_1.resample('A').mean()
    data_2=data_2['1990-12-31':'2010-12-31']
    data_2.index=air_sum.index
    
    data_3=data_1.resample('M').mean()
    data_sum=pd.concat([air_sum,data_2],axis=1)
    data_sum.rename(columns={0:'Total GHG'})
    data_sum=(data_sum-data_sum.min())/(data_sum.max()-data_sum.min())

    fig=plt.subplot(2,2,1)
    plt.xlabe('Years')
    plt.ylabel('Values')
    data_sum.plot(kind='line',ax=fig)

    fig=plt.subplot(2,2,2)
    plt.xlabel('Years')
    plt.ylabel('Values')
    data_sum.plot(kind='bar',ax=fig)

    fig=plt.subplot(2,2,3)
    plt.xlabel('Quarters')
    plt.ylabel('Temperature')
    data_3.plot(kind='area',ax=fig)

    fig=plt.subplot(2,2,4)
    plt.xlabel('Values')
    plt.xlabel('Values')
    data_3.plot(kind='kde',ax=fig)

    plt.tight_layout()
    plt.show()

    return fig

if __name__=='__main__':
    climate_plot()
