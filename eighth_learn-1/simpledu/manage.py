from simpledu.app import create_app
#创建对应变量app并运行
app=create_app('development')

if __name__ =='__main__':
    app.run()
