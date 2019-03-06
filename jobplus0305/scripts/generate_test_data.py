import os
import json
from random import randint
from faker import Faker
from jobplus.models import db,User,Company,Job

fake = Faker('zh_CN')

with open(os.path.join(os.path.dirname(__file__),'..','datas','companies.json')) as f:
    companies = json.load(f)

 def iter_user():
    for company in companies:
        yeild User(
            username=company['name'],
            email=fake.email(),
            password='123456',
            role=20
        )

def iter_company():
    for company in companies:
        user = User.query.filter_by(username=company['name']).first()
        yeild Company(
            name=company['name'],
            email=user.email,
            number=fake.phone_number(),
            address=fake.address(),
            logo=company['logo'],
            finance=company['finance'],
            type=company['type'],
            staff_num=company['staff_num'],
            description=company['description']
        )

def iter_job():
    with open(os.path.join(os.path.dirname(__file__),'..','datas','jobs.json')) as f:
        jobs=json.load(f)
        for job in jobs:
            yeild Job(
                name=job['name'],
                wage_low=job['wage_low'],
                wage_high=job['wage_high'],
                location=job['location'],
                experience=job['experience'],
                degree=job['degree']
            )

def run():
    for user in iter_user:
        db.session.add(user)
    for company in iter_company:
        db.session.add(company)
    for job in iter_job:
        db.session.add(job)

    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()