import hashlib
import os

from . import ModelMixin
from . import db


class User(db.Model, ModelMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    passworld = db.Column(db.String())
    admin = db.Column(db.Integer, default=10)
    weibos = db.relationship('Weibo', backref='user')
    comments = db.relationship('Comment', backref='user')


    def __init__(self, form):
        print('传入生成用户的form数据：', form)
        self.username = form.get('username', '')
        self.passworld = form.get('passworld', '')
        self.admin = form.get('admin', 10)

    # 更新用户密码
    def _update(self, form):
        print('user update', self, form)
        self.passworld = form.get('passworld', 123)

    # 用户名不重
    def valid_username(self, username):
        return User.query.filter_by(username=self.username).first() == None

    # 验证注册用户：要有不重的用户名，密码长度大于6
    def valid_register(self):
        valid_username = self.valid_username(self.username)
        print('名字重名吗：',valid_username)
        valid_username_len = len(self.username) >= 0
        valid_password_len = len(self.passworld) >= 6
        msgs = []
        if not valid_username:
            message = '用户名已经存在'
            msgs.append(message)
        if not valid_username_len:
            message = '必须填写用户名'
            msgs.append(message)
        if not valid_password_len:
            message = '密码长度必须大于等于 6'
            msgs.append(message)
        status = valid_username and valid_username_len and valid_password_len
        print('注册有效吗：',status)
        return status, msgs

    # 验证登录用户：密码和名字相同
    def valid_login(self):
        user = User.query.filter_by(username=self.username).first()
        print('根据名字查询出来的用户：',user)
        valid_pwd = (self.passworld == user.passworld)
        valid_user = not (user is None)
        msgs = []
        if not valid_user:
            msg = '用户不存在',
            msgs.append(msg)
        if not valid_pwd:
            print('密码输入错误!')
            msg = '密码输入错误',
            msgs.append(msg)
        status = valid_pwd and valid_user
        print('登录信息：',msgs)
        return status, msgs