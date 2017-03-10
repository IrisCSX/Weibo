from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


from models import db

from models.weibo import Weibo
from models.user import User
from models.comment import Comment



app = Flask(__name__)
manager = Manager(app)


def configured_app():
    """
    配置数据库路径
    secret_key
    注册路由
    初始化操作数据库的db
    生成配置日志
    :return:
    """
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    import config
    app.secret_key = config.secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = config.db_uri
    db.init_app(app)
    register_routes(app)
    configure_log(app)
    return app


def configure_log(app):
    if not app.debug:
        import logging
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)


def configure_manager():
    """
    增加数据库迁移命令的配置
    """
    Migrate(app, db)
    manager.add_command('db', MigrateCommand)


def register_routes(app):
    """
    注册蓝图
    """
    from routes.weibo import main as routes_todo
    app.register_blueprint(routes_todo, url_prefix='/weibo')

    from routes.user import main as routes_user
    app.register_blueprint(routes_user, url_prefix='/user')

    from routes.comment import main as routes_user
    app.register_blueprint(routes_user, url_prefix='/comment')

    from routes import main as routes_all
    app.register_blueprint(routes_all)


@manager.command
def server():
    """
    启动程序
    """
    app = configured_app()
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=3000,
    )
    app.run(**config)



@app.template_filter()
def format_time(updatetime):
    import time
    print('传入过滤器的时间是', updatetime)
    print('系统当前的时间是：', int(time.time()))
    format = '%m/%d %H:%M:%S'
    value = time.localtime(updatetime)
    return time.strftime(format, value)


if __name__ == '__main__':
    # configure_manager()
    # configured_app()
    manager.run()