from . import faqs as f
from flask_login import login_required,current_user
from .forms import ContactForm
from flask import render_template,abort,redirect,url_for,request,flash
@f.route("/faqs")
def bussiness_idea():
    return render_template("FAQS/bussiness.html")


@f.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()

  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('FAQS/contact.html', form=form)
    else:
      return 'Form posted.'

  elif request.method == 'GET':
    return render_template('FAQS/contact.html', form=form)
