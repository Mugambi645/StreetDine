
from . import cart as c
import flask
from flask_login import login_required,current_user
from flask import render_template,abort,redirect,url_for,request
from app.auth.models import Role,User
from app.profile.forms import UpdateProfile
from .. import db,photos
from app.auth.models import User
from .forms import SellForm
from .models import Sell
from app.profile.forms import UpdateProfile

@c.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_sale():
    sale_form = SellForm()
    if sale_form.validate_on_submit():
        title = sale_form.title.data
        sale = sale_form.text.data
        category = sale_form.category.data
        # Updated sale instance
        new_sale = Sell(sell_title=title,sell_content=sale,category=category, likes=0,dislikes=0)

        # Save sale method
        new_sale.save_sale()
        return redirect(url_for('main.index'))

    title = 'New sale'
    return render_template('cart/new_sell.html',title = title,sale_form=sale_form )




@c.route('/user/<uname>/items')
def user_items(uname):
    user = User.query.filter_by(username=uname).first()
    pitches = Sell.query.filter_by(user_id = user.id).all()
    sales_count = Sell.count_sale(uname)
    

    return render_template("cart/user_items.html", user=user,pitches=pitches,sales_count= sales_count)

