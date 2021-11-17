from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required
class ContactForm(FlaskForm):

    name = StringField('Name',validators=[Required("Please enter your name")])
    email = TextAreaField('Text',validators=[Required("Please enter a valid email address")])
    subject = TextAreaField('Text',validators=[Required("Enter a subject")])
    message = TextAreaField('Comment',validators=[Required("Please enter your reason for contact")])
    submit = SubmitField('Submit')
