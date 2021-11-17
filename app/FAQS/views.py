from . import faqs as f
from flask_login import login_required,current_user
from .forms import ContactForm
from flask import render_template,abort,redirect,url_for,request,flash
@f.route("/faqs")
def bussiness_idea():
    return render_template("FAQS/bussiness.html")


@f.route('/about', methods=['GET', 'POST'])
def about():
    return render_template("FAQS/about.html")