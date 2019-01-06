from flask import Flask
from flask import render_template
import os
import json
from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@localhost/shiyanlou'
db=SQLAlchemy(app)

class File(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(80))
    created_time=db.Column(db.DateTime)
    category_id=db.Column(db.Integer,db.ForeignKey('category.id'))
    category=relationship('Category',backref='find')
    content=db.Column(db.Text)
    def __init__(self,title,created_time,category,content):
        self.title=title
        self.created_time=datetime.utcnow()
        self.category=category
        self.content=content
    def __repr__(self):
        return '%r' % self.title

class Category(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return '%r' % self.name


#@app.route('/')
#def index():
#    title_list=os.listdir('/home/shiyanlou/files/')
#    file_name=[]
#    for i in title_list:
#        a=i.split('.')
#        file_name.append(a[0])
#    return render_template('index.html',file_name=file_name)

#@app.route('/files/<filename>')
#def file(filename):
#    if os.path.exists('/home/shiyanlou/files/'+ filename +'.json')
#        with open('/home/shiyanlou/files/'+filename+'.json','r') as f:
#            file_content=json.load(f)
#            file_print=file_content['content']
#        return render_template('file.html',file_print=file_print)
#    else:
#        return render_template('404.html'),404
#@app any('/<anything>')
#def any(anything):
#    return render_template('404.html'),404

