#定义基类，所有其他环境都继承这个基类
class BaseConfig(object):
    SECRET_KEY='secret key'

#定义开发环境变量
class DevelopmentConfig(BaseConfig):
    DEBUG=1
    SQLALCHEMY_DATABASE_URI='mysql+mysqldb://root@localhost:3306/simpledu?charset=utf8'
#生产环境
class ProductionConfig(BaseConfig):
    pass
#测试环境
class TestingConfig(BaseConfig):
    pass
#将所有环境类函数写成一个字典，别设置调用key值，在app.py中调用
configs={
        'development':DevelopmentConfig,
        'production':ProductionConfig,
        'testing':TestingConfig
}
