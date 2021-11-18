from .. import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin,login_manager
from app.auth.models import User
from datetime import datetime
class Articles(db.Model):
    __tablename__='articles'
    
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(2550))
    title = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    #reviews = db.relationship('Reviews', backref = 'author', lazy = True) 

    def save_article(self):
        db.session.add(self)
        db.session.commit()
    

    def __repr__(self):
        return f'Articles{self.name}'
