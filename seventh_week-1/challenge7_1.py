#_*_ coding:utf-8 _*_

import pandas as pd
import numpy as np
def co2():
    #提取文件
    df_climate=pd.read_excel("ClimateChange.xlsx", sheetname='Data')
    #查询指定值，并设置一个共用属性作为索引
    data=df_climate[df_climate['Series code'] == 'EN.ATM.CO2E.KT'].set_index('Country code')
    #去掉多余列，方便计算
    data=data.drop(['Country name','Series code','Series name','SCALE','Decimals'],axis=1)
#    data.drop(data.columns[:5], axis=1, inplace=True)
    #替换掉..的值，换为NaN，注意计算时NaN会当作0来计算，如果一行全是NaN，则计算结果为0，而不是NaN，所以如果要去控制需要在计算前就去掉，否则就不会去掉了
    data=data.replace({'..':pd.np.nan})
    #向前向后填充空值
    data=data.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    #计算没行的和
    data_sum=data.sum(axis=1)
    
    #提取另一个表
    df_country=pd.read_excel("ClimateChange.xlsx", sheetname='Country')
    #和前面的表设置相同索引，方便合并
    df_country.index=df_country['Country code']
    #提取出要用的列
    country=df_country['Income group']
    #合并表
    df_sum=pd.concat([data_sum,country],axis=1)
    #分组求和,得到第一个值，并设定列名
    df_sum_data=df_sum.groupby('Income group').sum()
    df_sum_data.columns=['Sum emissions']
    #添加一行城市名称
    df_sum['new']=df_country['Country name']
    #调整一下列的顺序，跟要求一样
    df_sum=df_sum.reindex(columns=['new',0,'Income group'])
#    df_sum=df_sum.dropna()
    #用值排序，然后用'Income group'分组，去第一个，并设置要求的索引，最后修改列名
    highest=df_sum.sort_values(0,ascending=False).groupby('Income group').head(1).set_index('Income group')
    highest.columns=['Highest emission country','Highest emissions']
    #此处的筛选，如果前面没有在求和前去除全空的行，这一步就是必须的，不然0就是最小的
    lowest=df_sum[df_sum[0]>0].sort_values(0).groupby('Income group').head(1).set_index('Income group')
    lowest.columns=['Lowest emission country','Lowest emissions']
    #合并结果
    results=pd.concat([df_sum_data,highest,lowest],axis=1)
    return results

if __name__=='__main__':
    co2()
