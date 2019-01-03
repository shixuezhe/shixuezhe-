from flask import Flask
from flask import render_template
import os
import json

app= Flask(__name__)

@app.route('/')
def index():
    title_list=os.listdir('/home/shiyanlou/files/')
    file_name=[]
    for i in title_list:
        a=i.split('.')
        file_name.append(a[0])
    return render_template('index.html',file_name=file_name)

@app.route('/files/<filename>')
def file(filename):
    if os.path.exists('/home/shiyanlou/files/'+ filename +'.json')
        with open('/home/shiyanlou/files/'+filename+'.json','r') as f:
            file_content=json.load(f)
            file_print=file_content['content']
        return render_template('file.html',file_print=file_print)
    else:
        return render_template('404.html'),404
@app any('/<anything>')
def any(anything):
    return render_template('404.html'),404

