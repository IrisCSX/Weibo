import time

from . import ModelMixin
from . import db


class Comment(db.Model, ModelMixin):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    updated_time = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    weibo_id = db.Column(db.Integer, db.ForeignKey('weibos.id'))

    def __init__(self, form):
        print('传入生成评论的form数据：', form)
        self.content = form.get('content', '')
        self.updated_time = int(time.time())


