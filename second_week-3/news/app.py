from flask import Flask
from flask import render_template
import os
import json
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from pymongo import MongoClient

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@localhost/shiyanlou'
db=SQLAlchemy(app)
client=MongoClient('127.0.0.1',27017)
da=client.shiyanlou

class File(db.Model):
    __tablename__='files'

    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(80))
    created_time=db.Column(db.DateTime)
    category_id=db.Column(db.Integer,db.ForeignKey('categories.id'))
    category=db.relationship('Category',uselist=False)
    content=db.Column(db.Text)
    def __init__(self,title,created_time,category,content):
        self.title=title
        self.created_time=datetime.utcnow()
        self.category=category
        self.content=content
    def add_tag(self,tag_name):
        file_item=da.files.find_one({'file_id':self.id})
        if file_item:
            tags=file_item['tags']
            if tag_name not in tags:
                tags.append(tag_name)
            da.files.update_one({'file_id':self.id},{'$set':{'tags':tags}})
        else:
            tags=[tag_name]
            da.files.insert_one({'file_id':self.id,'tags':tags})
        return tags
    def remove_tag(self,tag_name):
        file_item=da.files.find_one({'file_id':self.id})
        if file_item:
            tags=file_item['tags']
            try:
                tags.remove(tag_name)
                new_tags=tags
            except ValueError:
                return tags
            da.files.update_one({'file_id':self.id},{'$set':{'tags':new_tags}})
            return new_tags 
        else:
            return []
    @property
    def tags(self):
        file_item=da.files.find_one({'file_id':self.id})
        if file_item:
            return file_item['tags']
        else:
            return []

class Category(db.Model):
    __tablename__='categories'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    files=db.relationship('File')
    def __init__(self,name):
        self.name=name

def insert_data():
    java=Category('Java')
    python=Category('Python')
    file1=File('Hello Java', datetime.utcnow(),
            java, 'File Content - Java is cool!')
    file2=File('Hello Python', datetime.utcnow(),
            python, 'File Content - Python is cool!')
    db.session.add(java)
    db.session.add(python)
    db.session.add(file1)
    db.session.add(file2)
    db.session.commit()
    file1.add_tag('tech')
    file1.add_tag('java')
    file1.add_tag('linux')
    file2.add_tag('tech')
    file2.add_tag('python')

@app.route('/')
def index():
    return render_template('index.html',files=File.query.all())

@app.route('/files/<int:file_id>')
def file(file_id):
    file_find=File.query.get_or_404(file_id)
    return render_template('file.html',file_find=file_find)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__=='__main__':
    app.run()
