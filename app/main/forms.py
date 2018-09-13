from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):
    blog = TextAreaField('Your Blog')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    author = StringField('Author',validators=[Required()])
    comment = TextAreaField('Your Comment')
    submit = SubmitField('Submit')