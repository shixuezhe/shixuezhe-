#_*_ coding:utf-8 _*_

import pandas as pd

def quarter_volume():
    data=pd.read_csv('/home/shiyanlou/Code/apple.csv',header=0)
    data_analysis=data.Volume
    data_analysis.index=pd.to_datetime(data.Date)
    second_volume=data_analysis.resample('Q').sum().sort_values()[-2]
    return second_volume
