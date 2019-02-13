#_*_ coding:utf-8 _*_
import pandas as pd
import matplotlib as plt
import seaborn as sns

#数据包含四项，创建时间，课程名称，学习人数，学习时间，用逗号分隔，用pandas读取出来成为DataFrame的格式
courses=pd.read_table('courses.txt',sep=',',header=0)

#用to_datetime将创建时间提取出来，用作新表的索引，用旧表数据，但是会多出一行创建时间，所以要删除

i=pd.to_datetime(courses['创建时间'])
courses_ts=pd.DateFrame(data=courses.values,columns=courses.columns,index=i)
courses_ts=courses_ts.drop('创建时间',axis=1)

#对数据进行降频处理，用周次，并进行求和
courses_ts_W=courses_ts.resample('W').sum()

#用matplotlib绘制图形用一个函数
def mat_figure():
    plt.plot_date(courses_ts_W.index,courses_ts_W['学习时间'],'-')
    plt.xlabel('Time Series')
    plt.ylabel('Study Time')
    plt.show()
#用matplotlib绘制的图形比较乱，不能清楚反映趋势

#用seaborn绘制
def sea_figure():
    #引入一个序数列，方便绘制散点图
    courses_ts_W['id']=range(0,len(courses_ts_W.index.values))
    #这里用到了seaborn的绘图方式regplot，首先写入xy的参数，指定数据来源，设置散点图的参数，禁用置信区间绘制
    sns.regplot('id','学习时间',data=courses_ts_W,scatter_kws={'s':10},order=5,ci=None,truncate=True)
    plt.xlabel('Time Series')
    plt.ylabel('Study Time')
    plt.show()

#还可以通过x_bins=参数来绘制更直接反映升降的图像
def sea_figure_new():
    sns.regplot('id','学习人数',data=courses_ts_W,x_bins=10)
    plt.xlabel('Time Series')
    plt.ylabel('Study Time')
    plt.show()

#实验数据分析
def analysis():
    #分析数据前可以复制一份出来，减少对原数据的影响
    course_ts_A=courses_ts.copy()
    #计算平均学习时间并添加进去
    courses_ts_A['平均学习时间']=courses_ts_A['学习时间']/courses_ts_A['学习人数']
    #对平均时间进行排序
    a=course_ts_A.sort_values(by='平均学习时间',ascending=False)
    #可以用a.head()和a.tail()分别查看前/后五条数据
    #用seaborn的jointplot绘制图形
    sns.jointplot('平均学习时间','学习人数',kind='scatter',data=courses_ts_A)
    plt.xlabel('Average Study Time')
    plt.ylabel('Number of Users')
    plt.show()


if __name__=='__main__':
    mat_figure()
