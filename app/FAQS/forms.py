from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required
class ContactForm(FlaskForm):

    title = StringField('Name',validators=[Required("Please enter your name")])
    text = TextAreaField('Comment',validators=[Required("Please enter your reason for contact")])
    submit = SubmitField('Submit')
