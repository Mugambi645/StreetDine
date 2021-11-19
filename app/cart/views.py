
from . import cart as c
import flask
from flask_login import login_required,current_user
from flask import render_template,abort,redirect,url_for,request
from app.auth.models import Role,User
from app.profile.forms import UpdateProfile
from .. import db,photos
from app.auth.models import User
from .forms import PitchForm,CommentForm
from .models import Pitch,Comment
from app.profile.forms import UpdateProfile



@c.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch():
    pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        title = pitch_form.title.data
        pitch = pitch_form.text.data
        category = pitch_form.category.data
        
        # Updated pitch instance
        new_pitch = Pitch(pitch_title=title,pitch_content=pitch,category=category,  user=current_user,likes=0,dislikes=0)

        # Save pitch method
        new_pitch.save_pitch()
        return redirect(url_for('main.index'))

    title = 'New pitch'
    return render_template('cart/new_sell.html',title = title,pitch_form=pitch_form )




@c.route('/pitches/drinks')
def drinks_sale():

    pitches = Pitch.get_pitches('drinks')

    return render_template("cart/drinks.html", pitches = pitches)
 

@c.route('/pitches/fruits')
def fruits_sale():

    pitches = Pitch.get_pitches('fruits')

    return render_template("cart/fruits.html", pitches = pitches)


@c.route('/pitches/foreign')
def foreign_sale():

    pitches = Pitch.get_pitches('foreign')

    return render_template("cart/foreign.html", pitches = pitches)



@c.route('/pitches/traditional')
def traditional_sale():

    pitches = Pitch.get_pitches('traditional')

    return render_template("cart/traditional.html", pitches = pitches)


@c.route('/pitch/snacks')
def snacks():

    pitches = Pitch.get_pitches('snacks')

    return render_template("cart/snacks.html", pitches = pitches)


@c.route('/pitch/<int:id>', methods = ['GET','POST'])
def pitch(id):
    pitch = Pitch.get_pitch(id)
    posted_date = pitch.posted.strftime('%b %d, %Y')

    if request.args.get("like"):
        pitch.likes = pitch.likes + 1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch/{pitch_id}".format(pitch_id=pitch.id))
                                

    elif request.args.get("dislike"):
        pitch.dislikes = pitch.dislikes + 1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch/{pitch_id}".format(pitch_id=pitch.id))

    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.text.data

        new_comment = Comment(comment = comment,user = current_user,pitch_id = pitch)

        new_comment.save_comment()


    comments = Comment.get_comments(pitch)

    return render_template("cart/good.html", pitch = pitch, comment_form = comment_form, comments = comments, date = posted_date)

@c.route('/user/<uname>/pitches')
def user_pitches(uname):
    user = User.query.filter_by(username=uname).first()
    pitches = Pitch.query.filter_by(user_id = user.id).all()
    pitches_count = Pitch.count_pitches(uname)
    

    return render_template("cart/user_items.html", user=user,pitches=pitches,pitches_count=pitches_count)

