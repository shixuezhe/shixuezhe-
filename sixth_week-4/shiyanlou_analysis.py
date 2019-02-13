#_*_ coding:utf-8 _*_
import pandas as pd
import matplotlib as plt
import seaborn as sns

#���ݰ����������ʱ�䣬�γ����ƣ�ѧϰ������ѧϰʱ�䣬�ö��ŷָ�����pandas��ȡ������ΪDataFrame�ĸ�ʽ
courses=pd.read_table('courses.txt',sep=',',header=0)

#��to_datetime������ʱ����ȡ�����������±���������þɱ����ݣ����ǻ���һ�д���ʱ�䣬����Ҫɾ��

i=pd.to_datetime(courses['����ʱ��'])
courses_ts=pd.DateFrame(data=courses.values,columns=courses.columns,index=i)
courses_ts=courses_ts.drop('����ʱ��',axis=1)

#�����ݽ��н�Ƶ�������ܴΣ����������
courses_ts_W=courses_ts.resample('W').sum()

#��matplotlib����ͼ����һ������
def mat_figure():
    plt.plot_date(courses_ts_W.index,courses_ts_W['ѧϰʱ��'],'-')
    plt.xlabel('Time Series')
    plt.ylabel('Study Time')
    plt.show()
#��matplotlib���Ƶ�ͼ�αȽ��ң����������ӳ����

#��seaborn����
def sea_figure():
    #����һ�������У��������ɢ��ͼ
    courses_ts_W['id']=range(0,len(courses_ts_W.index.values))
    #�����õ���seaborn�Ļ�ͼ��ʽregplot������д��xy�Ĳ�����ָ��������Դ������ɢ��ͼ�Ĳ��������������������
    sns.regplot('id','ѧϰʱ��',data=courses_ts_W,scatter_kws={'s':10},order=5,ci=None,truncate=True)
    plt.xlabel('Time Series')
    plt.ylabel('Study Time')
    plt.show()

#������ͨ��x_bins=���������Ƹ�ֱ�ӷ�ӳ������ͼ��
def sea_figure_new():
    sns.regplot('id','ѧϰ����',data=courses_ts_W,x_bins=10)
    plt.xlabel('Time Series')
    plt.ylabel('Study Time')
    plt.show()

#ʵ�����ݷ���
def analysis():
    #��������ǰ���Ը���һ�ݳ��������ٶ�ԭ���ݵ�Ӱ��
    course_ts_A=courses_ts.copy()
    #����ƽ��ѧϰʱ�䲢��ӽ�ȥ
    courses_ts_A['ƽ��ѧϰʱ��']=courses_ts_A['ѧϰʱ��']/courses_ts_A['ѧϰ����']
    #��ƽ��ʱ���������
    a=course_ts_A.sort_values(by='ƽ��ѧϰʱ��',ascending=False)
    #������a.head()��a.tail()�ֱ�鿴ǰ/����������
    #��seaborn��jointplot����ͼ��
    sns.jointplot('ƽ��ѧϰʱ��','ѧϰ����',kind='scatter',data=courses_ts_A)
    plt.xlabel('Average Study Time')
    plt.ylabel('Number of Users')
    plt.show()


if __name__=='__main__':
    mat_figure()
