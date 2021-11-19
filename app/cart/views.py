
from . import cart as c
import flask
from flask_login import login_required,current_user
from flask import render_template,abort,redirect,url_for,request
from app.auth.models import Role,User
from app.profile.forms import UpdateProfile
from .. import db,photos
from app.auth.models import User
from .forms import ArticleForm
from .models import Articles
from app.profile.forms import UpdateProfile
@c.route("/post",methods=['GET','POST'])
@login_required
def post():
    form = ArticleForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        new_post = Articles()
        new_post.title = title
        new_post.content= content

        new_post.save_article()

        new_article = Articles(title=title,content = content)
    
        return redirect(url_for('.buy'))

    title="Post your article"
    return render_template('cart/new_sell.html',title=title,article_form=form)


@c.route("/buy")
@login_required
def buy():
    return render_template("cart/buy.html")

@c.route('/user/<uname>/items')
def user_items(uname):
    user = User.query.filter_by(username=uname).first()
    pitches = Articles.query.filter_by(user_id = user.id).all()
    sales_count = Articles.count_sale(uname)
    

    return render_template("cart/user_items.html", user=user,pitches=pitches,sales_count= sales_count)

