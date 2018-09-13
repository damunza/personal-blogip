from flask import render_template, redirect,url_for
from flask_login import login_required, current_user
from . import main
from .forms import BlogForm
from ..models import Blog

@main.route('/')
def index():
    '''
    function that returns the index page
    '''
    blogs = Blog.query.all()
    return render_template('index.html', blogs = blogs)

@main.route('/new_blog', methods = ['GET','POST'])
@login_required
def new_blog():
   form  =BlogForm()

   if form.validate_on_submit():
       blog = form.blog.data

       new_blog = Blog(blog = blog, user_id = current_user.id)

       new_blog.save_blog()

       return redirect(url_for('main.index'))

   title = 'New Blog'
   return render_template('new_blog.html',title = title, blog_form = form)
