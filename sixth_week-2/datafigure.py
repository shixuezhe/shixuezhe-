import json
import pandas as pd
from  matplotlib import pyplot as plt

def data_plot():

    data=pd.read_json('/home/shiyanlou/Code/user_study.json')
    data_new=data.groupby('user_id').sum()
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.set_title('StudyData')
    ax.set_xlabel('User ID')
    ax.set_ylabel('Study Time')
    ax.plot(data_new.index,data_new.minutes)
    plt.show()
    return ax

if __name__=='__main__':
    data_plot()
