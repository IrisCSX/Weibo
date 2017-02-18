from models.comment import Comment

from routes import *


main = Blueprint('comment', __name__)

Model = Comment


@main.route('/add', methods=['POST'])
def add():
    user = curr_user()
    weibo_id = request.args.get('weiboid')
    form = request.form
    model = Model.new(form)
    model.user_id = user.id
    model.weibo_id = weibo_id
    model.save()
    return redirect(url_for('weibo.index',id=weibo_id))









