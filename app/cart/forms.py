from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required
class PitchForm(FlaskForm):

    title = StringField('Sale title',validators=[Required()])
    text = TextAreaField('Text',validators=[Required()])
    category = SelectField('Type',choices=[('drinks','Drinks and beverages'),('fruits','Fruits'),('foreign','Foreign Dishes'), ('traditional', 'Traditional Dishes'), ('snacks', 'Snacks')],validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    text = TextAreaField('Leave a comment:',validators=[Required()])
    submit = SubmitField('Submit')