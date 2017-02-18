from flask import Blueprint
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request
from flask import send_from_directory
from flask import session
from flask import url_for
from flask import abort
from models.user import  User
from functools import wraps
import time


main = Blueprint('enter', __name__)


@main.route('/')
def enter():
    return render_template('user/enter.html')


def curr_user():
    uid = session.get('user_id')
    print('当前得到的用户的session',session)
    if uid is not None:
        u = User.query.get(uid)
        return u


def login_required(f):
    print('login required')
    @wraps(f)
    def function(*args, **kwargs):
        print('current user check', curr_user())
        if curr_user() is None:
            return redirect(url_for('user.enter'))
        else:
            return f(*args, **kwargs)
    return function