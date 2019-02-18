from flask import Flask,render_template
from simpledu.config import configs
from simpledu.models import db,Course

def create_app(config):
    #创建工厂函数，传入变量类型参数
    app=Flask(__name__)
    app.config.from_object(configs.get(config))
    #init_app是sqlalchemy的传入参数，直接创建为sqlalchemy(app),分开了就必须要使用init_app参数
    db.init_app(app)
    #创建蓝图
    register_blueprints(app)
    return app
#定义蓝图函数
def register_blueprints(app):
    from .handlers import front,course,admin
    app.register_blueprint(front)
    app.register_blueprint(course)
    app.register_blueprint(admin)




