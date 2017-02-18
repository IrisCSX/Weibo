from models.user import User

from routes import *


main = Blueprint('user', __name__)

Model = User



# @main.route('/')
# def enter():
#     return render_template('user/enter.html')


@main.route('/register', methods=['POST'])
def register():
    form = request.form
    model = Model(form)
    statu, msgs = model.valid_register()
    msg = '   '.join(msgs)
    if statu:
        model = Model.new(form)
        session['user_id'] = model.id
        return redirect(url_for('weibo.all'))
    else:
        # abort(404)
        return render_template('user/enter.html', login_msg=msg)

@main.route('/login', methods=['POST'])
def login():
    form = request.form
    model = Model(form)
    statu, msgs = model.valid_login()
    print('登录结果：',msgs)
    if statu:
        model = User.query.filter_by(username=model.username).first()
        session['user_id'] = model.id
        return redirect(url_for('weibo.all'))
    else:
        # abort(404)
        return render_template('user/enter.html', register_msg=msgs[-1])


@main.route('/index')
def index():
    user = curr_user()
    weibos = user.weibos
    print('登录用户发的微博：',weibos)
    return render_template('/user/index.html', curr_user=user,  weibos=weibos)








