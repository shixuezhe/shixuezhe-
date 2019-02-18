#引入蓝图函数，在路由中用到的变量或函数也要引入
from flask import Blueprint,render_template
from simpledu.models import Course
#省略url_prefix，默认为'/'
front=Blueprint('front',__name__)

#使用对应蓝图的路由，不再是对应app了
@front.route('/')
def index():
    courses=Course.query.all()
    return render_template('index.html',courses=courses)
