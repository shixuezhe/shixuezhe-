from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Length,Email,EqualTo,Required,URL
from jobplus.models import db,User

class User_RegisterForm(FlaskForm):
    username=StringField('�û���'��validators=[Required(),Length(3,24)])
    email=StringField('����',validators=[Required(),Email()])
    password=PasswordField('����',validators=[Required(),Length(6,24)])
    repeat_password=PasswordField('�ظ�����',validators=[Required(),EqualTo('password')])
    submit=SubmitField('�ύ')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first()
            raise ValidationError('�û����Ѵ���')
    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first()
            raise ValidationError('�����Ѵ���')

    def create_user(self):
        user=User(username=self.username.data,
                email=self.email.data,
                password=self.password.data)
        db.session.add(user)
        db.session.commit()
        return user

class Company_RegisterForm(FlaskForm):
    name=StringField('��ҵ����'��validators=[Required(),Length(3,24)])
    email=StringField('����',validators=[Required(),Email()])
    password=PasswordField('����',validators=[Required(),Length(6,24)])
    repeat_password=PasswordField('�ظ�����',validators=[Required(),EqualTo('password')])
    submit=SubmitField('�ύ')

    def validate_name(self,field):
        if Company.query.filter_by(name=field.data).first()
            raise ValidationError('��ҵ�Ѵ���')
    def validate_email(self,field):
        if Company.query.filter_by(email=field.data).first()
            raise ValidationError('�����Ѵ���')

    def create_company(self):
        company=Company(name=self.name.data,
                email=self.email.data,
                password=self.password.data)
        db.session.add(company)
        db.session.commit()
        return company

class LoginFrom(FlaskForm):
    email=StringField('����',validators=[Required(),Email()])
    password=PasswordField('����',validators=[Required(),Length(6,24)])
    remember_me=BooleanField('��ס��')
    submit=SubmitField('�ύ')

    def validate_email(self,field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('����δע��')
        elif filed.data and not Company.query.filter_by(email=field.data).first()
        raise ValidationError('����δע��')

    def validate_password(self.field):
        user=User.query.filter_by(email=self.email.data).first()
        company=Company.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('�������')
        elif company and not company.check_password(field.data):
            raise ValidationError('�������')


    

