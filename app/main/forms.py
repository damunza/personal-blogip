from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class BlogForm(FlaskForm):
    blog = TextAreaField('Your Blog')
    submit = SubmitField('Submit')