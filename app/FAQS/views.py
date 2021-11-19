from . import faqs as f
from flask_login import login_required,current_user,session_protected
from .forms import ContactForm
from flask import render_template,abort,redirect,url_for,request,flash,session
@f.route("/faqs")
def bussiness_idea():
    return render_template("FAQS/bussiness.html")


@f.route('/about', methods=['GET', 'POST'])
def about():
    return render_template("FAQS/about.html")


@f.route('/about', methods=['GET', 'POST'])
def contact():
    session['firstname'] = request.form.get('firstname')
    session['lastname'] = request.form.get('lastname')
    session['email'] = request.form.get('email')
    session['subject'] = request.form.get('subject')
    session['message'] = request.form.get('message')
    print(session['firstname'], session['lastname'], session['email'], session['subject'],session['message'])
    if session['firstname'] != None:
        flash(f'Message sent!', 'success')
    return render_template('FAQS/about.html', tilte = 'Contact')