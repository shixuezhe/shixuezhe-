from flask import Blueprint, render_template
from simpledu.models import Course,User
from simpledu.forms import LoginForm,RegisterForm
from flask import flash,redirect,url_for
from flask_login import login_user,logout_user,login_required
from flask import request,current_app

front = Blueprint('front', __name__)

@front.route('/')
def index():
    #获取参数中传过来的页数
    page=request.args.get('page',default=1,type=int)
    #生成分页对象
    pagination=Course.query.paginate(
            page=page,
            per_page=current_app.config['INDEX_PER_PAGE'],
            error_out=False
            )
    return render_template('index.html', pagination=pagination)

@front.route('/login')
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        login_user(user,form.remember_me.data)
        return redirect(url_for('.index'))
    return render_template('login.html',form=form)

@front.route('/register',methods=['POST','GET'])
def register():
    form=RegisterForm()
    if form.validate_on_submit():
        #使用isalnum判断是否所数字和字母并flash错误
        if not form.username.data.isalnum():
            flash('用户名只能使用数字和字母')
            return redirect(url_for('.register'))
        form.create_user()
        flash('注册成功,请登录！','success')
        return redirect(url_for('.login'))
    return render_template('register.html',form=form)

@front.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已退出登录','success')
    return redirect(url_for('.index'))
