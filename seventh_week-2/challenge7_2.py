#_*_ coding:utf-8 _*_

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def co2_gdp_plot():
    #数据读取，更换索引，处理缺失值
    data= pd.read_excel("ClimateChange.xlsx", sheetname='Data')
    df_gdp=data[data['Series code'] == 'NY.GDP.MKTP.CD'].set_index('Country code')
    df_gdp=df_gdp.drop(df_gdp.columns[:5],axis=1)
    df_gdp=df_gdp.replace({'..':pd.np.nan})
    #df_gdp.dropna(how='all')
    df_gdp=df_gdp.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    df_gdp=df_gdp.sum(axis=1)

    df_co2=data[data['Series code'] == 'EN.ATM.CO2E.KT'].set_index('Country code')
    df_co2=df_co2.drop(df_co2.columns[:5],axis=1)
    df_co2=df_co2.replace({'..':pd.np.nan})
    df_co2=df_co2.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    df_co2=df_co2.sum(axis=1)

    #合并数据，更改列名
    df_sum=pd.concat([df_co2,df_gdp],axis=1)
    df_sum.columns=['CO2-SUM','GDP-SUM']
    df_sum.replace({pd.np.nan:0})
    #df_sum=df_sum.fillna(value=0)
    df_mat=(df_sum-df_sum.min())/(df_sum.max()-df_sum.min())
#    print(df_mat)

    #由于要设置坐标刻度，但是每个国家代码都在索引里面，所以要把他们提取出来，需要一个位置和标签
    xtick_range=[]
    xtick_label=[]
    five_countries = ['USA', 'CHN', 'FRA', 'RUS', 'GBR']
    for i in range(len(df_mat)):
        if df_mat.index[i] in five_countries:
            xtick_range.append(i)
            xtick_label.append(df_mat.index[i])
#    print(xtick_range,xtick_label)
    
    #作图，设置画布，在绘图时指定该画布
    fig =plt.subplot()
    df_mat.plot(kind='line',ax=fig)
    #补充一下，画布才有set属性，plt没有的
    fig.set_title('GDP-CO2')
    fig.set_xlabel('Countries')
    fig.set_ylabel('Values')
    #对plt设置时是没有set前缀的，格式为范围信息(xtick_range)，然后所是标签内容(xtick_label),rotation为旋转属性，'vertical‘的意思是垂直
    plt.xticks(xtick_range,xtick_label,rotation='vertical')
    plt.show()
    
    #提取中国的信息
    co2_data=df_mat.loc['CHN','CO2-SUM']
    gdp_data=df_mat.loc['CHN','GDP-SUM']
    #设置精度并加入列表
    china=[float('%.3f' % co2_data),float('%.3f' % gdp_data)]
#    print(china)
    return fig,china

if __name__=='__main__':
    co2_gdp_plot()
