from flask import Flask
import os,json
from flask import render_template,abort

app=Flask(__name__)
#后面都要用到文件内容字典，所以写一个获取函数
def get_titles():
    files={}
    for i in os.listdir('/home/shiyanlou/files'):
        with open('/home/shiyanlou/files/'+i,'r') as f:
            files[i[:-5]]=json.load(f)
    return files
#filename有一个后缀，所以用切片的方式去除
@app.route('/')
def index():
    files=get_titles()
    titles=[item['title'] for item in files.values()]
    return render_template('index.html',titles=titles)

@app.route('/files/<filename>')
def file(filename):
    files=get_titles()
    file_content=files.get(filename)
    if file_content is None:
        abort(404)
    return render_template('file.html',file_content=file_content)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__=='__main__':
    app.run()
