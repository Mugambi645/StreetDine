from . import faqs as f
from flask_login import login_required,current_user
from flask import render_template,abort,redirect,url_for,request
@f.route("/faqs")
def bussiness_idea():
    return render_template("FAQS/bussiness.html")
