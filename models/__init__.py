from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import time

db = SQLAlchemy()

app = Flask(__name__)
app.secret_key = 'secret key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weibos.db'

db = SQLAlchemy(app)

def timestamp():
    return int(time.time())


class ModelMixin(object):
    @classmethod
    def new(cls, form):
        m = cls(form)
        m.save()
        return m

    @classmethod
    def update(cls, model_id, form):
        m = cls.query.get(model_id)
        print('update cls method', m, model_id)
        m._update(form)
        m.save()

    @classmethod
    def delete(cls, model_id):
        m = cls.query.get(model_id)
        m.remove()

    @classmethod
    def all(cls):
        return cls.query.all()

    # 打印子类的属性和属性值
    def __repr__(self):
        class_name = self.__class__.__name__
        properties = ('{0} = {1}'.format(k, v) for k, v in self.__dict__.items())
        return '<{0}: \n  {1}\n>'.format(class_name, '\n  '.join(properties))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()
        # self.deleted = True
        # self.save()
