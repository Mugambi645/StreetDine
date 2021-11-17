from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class SellForm(FlaskForm):

    title = StringField('Food Description',validators=[Required()])
    text = TextAreaField('Text',validators=[Required()])
    category = SelectField('Type',choices=[('drinks','Drinks'),('snacks','Snacks'),('regular_food','Regular Food'), ('traditional_dishes', 'Traditional Dishes'), ('foreign_dishes', 'Foreign Dishes')],validators=[Required()])
    submit = SubmitField('Submit')
