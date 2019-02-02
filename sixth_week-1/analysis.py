import json
import pandas as pd

def analysis(file,user_id):
    times=0
    minutes=0
    try:
        data=pd.read_json(file) 
        df=pd.DataFrame(data)
    except:
        return times,minutes

    data_times=df[df['user_id'] ==user_id]['user_id'].count()
    times += int(data_times)

    data_minutes=df[df['user_id'] == user_id]['minutes'].sum()
    minutes += int(data_minutes)
    return times,minutes
#    print(times,minutes)

if __name__ == '__main__':
    analysis('/home/shiyanlou/Code/user_study.json',199071)
