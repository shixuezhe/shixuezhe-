from flask import url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

db = SQLAlchemy()

user_job = db.Table(
        'user_job',
        db.Column('user_id',db.Integer,db.ForeignKey('user.id',ondelete='CASCADE')),
        db.Column('job_id',db.Integer,db.ForeignKey('job.id',ondelete='CASCADE')))

class Base(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)

class User(Base,UserMixin):
    __tablename__ = 'user'
    ROLE_USER = 10
    ROLE_COMPANY = 20
    ROLE_ADMIN = 30
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(32),unique=True,index=True,nullable=False)
    email = db.Column(db.String(64),unique=True,index=True,nullable=False)
    _password = db.Column('password',db.String(256),nullable=False)
    phone_number = db.Column(db.Integer)
    resume = db.Column(db.String(128))
    experience = db.Column(db.String(24))
    role = db.Column(db.SmallInteger,default=ROLE_USER)
    user_jobs = db.relationship('Job',secondary=user_job)
    detail = db.relationship('Company',uselist=False)

    def __repr__(self):
        return '<User:{}>'.format(self.username)

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self,orig_password):
        self._password = generate_password_hash(orig_password)

    def check_password(self,password):
        return check_password_hash(self._password, password)

    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    @property
    def is_company(self):
        return self.role == self.ROLE_COMPANY
    

class Company(Base):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128),unique=True,index=True,nullable=False)
    email = db.Column(db.String(64),nullable=False)
    number = db.Column(db.String(48),nullable=False)
    slug = db.Column(db.String(64),unique=True,index=True,nullable=False)
    address = db.Column(db.String(128),nullable=False)
    site = db.Column(db.String(64),nullable=False)
    logo = db.Column(db.String(128),nullable=False)
    description = db.Column(db.String(64))
    details = db.Column(db.Text())
    tags = db.Column(db.String(64))
    location = db.Column(db.String(32))
    users_id = db.Column(db.Integer,db.ForeignKey('user.id',ondelete='CASCADE'))
    users = db.relationship('User',uselist=False,backref=db.backref('companies',uselist=False))

    def __repr__(self):
        return '<Company {}>'.format(self.name)

    
class Job(Base):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),nullable=False)
    wage_low = db.Column(db.Integer,nullable=False)
    wage_high = db.Column(db.Integer,nullable=False)
    location = db.Column(db.String(32),nullable=False)
    tags = db.Column(db.String(64))
    experience = db.Column(db.String(64))
    degree = db.Column(db.String(64))
    is_fulltime = db.Column(db.Boolean,default=True)
    is_open = db.Column(db.Boolean,default=True)
    description = db.Column(db.Text())
    company_id = db.Column(db.Integer,db.ForeignKey('company.id',ondelete='CASCADE'))
    companies = db.relationship('Company',uselist=False)
    view_count = db.Column(db.Integer,default=0)
    
    def __repr__(self):
        return '<Job:{}>'.format(self.name)

class Delivery(Base):
    STATUS_WAITING = 1
    STATUS_REJECT = 2
    STATUS_ACCEPT = 3

    id = db.Column(db.Integer,primary_key=True)
    job_id = db.Column(db.Integer,db.ForeignKey('job.id',ondelete='CASCADE'))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id',ondelete='CASCADE'))
    status = db.Column(db.SmallInteger,default=STATUS_WAITING)

