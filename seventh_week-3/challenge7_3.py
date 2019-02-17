import pandas as pd
import matplotlib.pyplot as plt

def climate_plot():
    #提取数据
    df_climate = pd.read_excel("ClimateChange.xlsx")
    l = ['EN.ATM.CO2E.KT','EN.ATM.METH.KT.CE','EN.ATM.NOXE.KT.CE',
         'EN.ATM.GHGO.KT.CE','EN.CLC.GHGR.MT.CE']
    #用isin的方法提取数据，用索引提取需要的列数据
    data = df_climate[df_climate['Series code'].isin(l)].iloc[:, 6:-1]
    #inplace参数是对原数据进行修改的意思
    data.replace({'..': pd.np.nan}, inplace=True)
    data = data.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1).sum()
    #求和生成的是Series数据，需要转换为DataFrame数据
    data = pd.DataFrame(data.values, index=data.index, columns=['Total GHG'])
    
    #提取温度数据
    gt = pd.read_excel("GlobalTemperature.xlsx")
    #设置日期为索引，提取两行数据，必须是日期才能用resample进行重采样
    gt = gt.iloc[:, [1, 4]].set_index(pd.to_datetime(gt.Date))
    gt.fillna(0, inplace=True)
    gt_year = gt.resample('a').mean()['1990': '2010']
    gt_qua = gt.resample('q').mean()
    df = pd.concat([gt_year.set_index(data.index), data], axis=1)
    #归一化数据
    df = df.apply(lambda x: (x-x.min())/(x.max()-x.min()))

    #折线图
    fig=plt.subplot(2,2,1)
    plt.xlabel('Years')
    plt.ylabel('Values')
    df.plot(kind='line',ax=fig)
    
    #柱状图
    fig=plt.subplot(2,2,2)
    plt.xlabel('Years')
    plt.ylabel('Values')
    df.plot(kind='bar',ax=fig)

    #面积图
    fig=plt.subplot(2,2,3)
    plt.xlabel('Quarters')
    plt.ylabel('Temperature')
    gt_qua.plot(kind='area',ax=fig)
    
    #密度图
    fig=plt.subplot(2,2,4)
    plt.xlabel('Values')
    plt.xlabel('Values')
    gt_qua.plot(kind='kde',ax=fig)
    
    #自动调整分布
    plt.tight_layout()
    plt.show()

    return fig

if __name__=='__main__':
    climate_plot()
