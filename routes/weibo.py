from models.weibo import Weibo

from routes import *


main = Blueprint('weibo', __name__)

Model = Weibo


@main.route('/')
def all():
    user = curr_user()
    models = Model.all()
    print("当前登录用户：", user)
    return render_template('weibo/weibos.html', curr_user=user, models=models)


@main.route('/index/<int:id>')
def index(id):
    model = Model.query.get(id)
    comments = model.comments
    user = model.user
    return render_template('weibo/index.html', weibo=model, comments=comments, user=user)


@main.route('/edit/<int:id>')
def edit(id):
    m = Model.query.get(id)
    return render_template('weibo/edit.html', model=m)


@main.route('/add', methods=['POST'])
@login_required
def add():
    form = request.form
    user = curr_user()
    model = Model.new(form)
    model.user_id = user.id
    model.save()
    return redirect(url_for('weibo.all'))


@main.route('/update/<int:id>', methods=['POST'])
@login_required
def update(id):
    form = request.form
    Model.update(id, form)
    model = Model.query.get(id)
    model.updated_time = int(time.time())
    model.save()
    return redirect(url_for('user.index'))


@main.route('/delete/<int:id>')
@login_required
def delete(id):
    Model.delete(id)
    return redirect(url_for('user.index'))
