from .. import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin,login_manager
from app.auth.models import User
from datetime import datetime

class Sell(db.Model):
    __tablename__ = 'sell'

    id = db.Column(db.Integer,primary_key = True)
    sell_title = db.Column(db.String)
    sell_content = db.Column(db.String(1000))
    category = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)
    #comments = db.relationship('Comment',backref =  'pitch_id',lazy = "dynamic")

    def __repr__(self):
        return f'User {self.sell_title}'
    
    def save_sale(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_sale(cls,category):
        sales = Sell.query.filter_by(category=category).all()
        return sales

    @classmethod
    def get_sale(cls,id):
        sales = Sell.query.filter_by(id=id).first()

        return sales

    @classmethod
    def count_sale(cls,uname):
        user = User.query.filter_by(username=uname).first()
        sales = Sell.query.filter_by(user_id=user.id).all()

        sales_count = 0
        for sale in sales:
            sales_count += 1

        return sales_count