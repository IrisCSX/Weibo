import time

from . import ModelMixin
from . import db


class Weibo(db.Model, ModelMixin):
    __tablename__ = 'weibos'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    updated_time = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref='weibo')

    def __init__(self, form):
        print('传入生成微博的form数据：', form)
        self.content = form.get('content', '')
        self.updated_time = int(time.time())

    # 更新微博内容
    def _update(self, form):
        self.content = form.get('content', '')
