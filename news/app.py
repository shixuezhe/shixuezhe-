from flask import Flask
from flask import render_template
import os
import json
from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from pymongo import MongoClient

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@localhost/shiyanlou'
db=SQLAlchemy(app)
client=MongoClient('127.0.0.1',27017)
da=client.shiyanlou

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
    def add_tag(self,tag_name):
        self.tag_name=tag_name
        mon_name=self.title
        da.mon_name.insert_one({mon_name:tag_name})
        label_dict=da.mon_name.find()
        return label_dict
    def remove_tag(self,tag_name):
        self.tag_name=tag_name
        mon_name=self.title
        da.mon_name.delete_one({mon_name:tag_name})
    def __repr__(self):
        return '%s' % self.title
    file_title=self.title
    return file_title
@property
def tags(self):
    tag_list=da.file_title.find()
    tag_content=[]
    for tag in tag_list:
        tag_content.append(tag_list[file_title])
        return tag_content
    
class Category(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return '%r' % self.name

title_list=File.query.all()
tags()
@app.route('/')
def index():
    return render_template('index.html',title_list=title_list,tag_content=tag_content)

@app.route('/files/<file_id>')
def file(file_id):
    file_find=File.query.filter(File.id==file_id).first()
    if file_find:
        return render_template('file.html',file_find=file_find)
    else:
        return render_template('404.html'),404

