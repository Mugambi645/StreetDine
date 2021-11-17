from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required
class ContactForm(FlaskForm):

    title = StringField('Name',validators=[Required()])
    text = TextAreaField('Comment',validators=[Required()])
    submit = SubmitField('Submit')
