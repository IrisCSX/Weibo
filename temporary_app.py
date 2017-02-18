import time
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from routes.weibo import main as routes_weibo
from routes.user import main as routes_user
from routes.comment import main as routes_comment
from routes import main as routes_all
from models import db


app = Flask(__name__)
manager = Manager(app)
app.secret_key = 'random string'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weibos.db'

app.register_blueprint(routes_weibo, url_prefix='/weibo')
app.register_blueprint(routes_user, url_prefix='/user')
app.register_blueprint(routes_comment, url_prefix='/comment')
app.register_blueprint(routes_all)


# 过滤器
@app.template_filter()
def format_time(updatetime):
    print('传入过滤器的时间是', updatetime)
    print('系统当前的时间是：', int(time.time()))
    format = '%m/%d %H:%M:%S'
    value = time.localtime(updatetime)
    return time.strftime(format, value)


def init_db():
    # 先 drop_all 删除所有数据库中的表
    # 再 create_all 创建所有的表
    db.drop_all()
    db.create_all()
    print('rebuild database')


def run():
    app.run(debug=True)

# 默认端口5000
if __name__ == '__main__':
    # init_db()
    run()

