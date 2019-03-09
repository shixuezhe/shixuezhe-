from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextField,ValidationError
from wtforms.validators import Required,Length,EqualTo,URL,Email
from jobplus.models import db,User,Company,Job,Delivery

class User_RegisterForm(FlaskForm):
    username = StringField('用户名',validators=[Required(),Length(3,24)])
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码',validators=[Required(),Length(6,24)])
    repeat_password = PasswordField('重复密码',validators=[Required(),EqualTo('password')])
    submit = SubmitField('提交')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已存在')
    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已存在')

    def create_user(self):
        user = User()
        self.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        return user

class Company_RegisterForm(FlaskForm):
    username = StringField('企业名称',validators=[Required(),Length(3,24)])
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码',validators=[Required(),Length(6,24)])
    repeat_password = PasswordField('重复密码',validators=[Required(),EqualTo('password')])
    submit = SubmitField('提交')

    def validate_name(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('企业已存在')
    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已存在')

    def create_company(self):
        user = User(
                username=self.username.data,
                email=self.email.data,
                password=self.password.data,
                role=20
                )
        db.session.add(user)
        db.session.commit()
        return user

class LoginForm(FlaskForm):
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码',validators=[Required(),Length(6,24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')

    def validate_email(self,field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱未注册')

    def validate_password(self,field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('密码错误')

class UserProfileForm(FlaskForm):
    username = StringField('用户名',validators=[Required(),Length(3,24)])
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码',validators=[Required(),Length(6,24)])
    phone_number = StringField('手机号',validators=[Required(),Length(11)])
    resume = StringField('简历链接',validators=[Required(),URL()])
    experience = StringField('工作年限')
    submit = SubmitField('提交')
    
    def validate_phone(self,field):
        if field.data[0] is not 1 and len(field.data) != 11:
            raise ValidationError('请输入正确11位手机号码')

    def update_user(self,user):
        user.username = self.username.data
        user.email = self.email.data
        if self.password.data:
            user.password = self.password.data
        user.phone_number = self.phone_number.data
        user.resume = self.resume.data
        user.experience = self.experience.data
        db.session.add(user)
        db.session.commit()

class CompanyProfileForm(FlaskForm):
    name = StringField('企业名称',validators=[Required(),Length(3,24)])
    email = StringField('邮箱',validators=[Required(),Email()])
    number = StringField('手机号',validators=[Required(),Length(11)])
    password = PasswordField('密码',validators=[Required(),Length(6,24)])
    slug = StringField('Slug',validators=[Length(3,24)])
    address = StringField('公司地址',validators=[Required(),Length(2,36)])
    site = StringField('公司网址',validators=[Length(9,36)])
    logo = StringField('logo',validators=[Required(),URL()])
    description = StringField('概述',validators=[Length(0,24)])
    details = TextField('公司详情',validators=[Length(0,256)])
    submit = SubmitField('提交')

    def validate_phone(self,field):
        if field.data[0] is not 1 and len(field.data) != 11:
            raise ValidationError('please input correct phone number')

    def update_company(self,user):
        user.username = self.name.data
        user.email = self.email.data
        if self.password:
            user.password = self.password.data
        if user.companies:
            companies = user.companies
        else:
            companies = Company()
            companies.users_id = user.id
        self.populate_obj(companies)
        db.session.add(user)
        db.session.add(companies)
        db.session.commit()