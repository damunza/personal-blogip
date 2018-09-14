from flask import render_template, redirect,url_for
from flask_login import login_required, current_user
from . import main
from .forms import BlogForm, CommentForm
from ..models import Blog, Comment, User

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

@main.route('/comment/<id>')
def comment(id):
    '''
    function to return the pitches
    '''
    comment = Comment.get_comment(id)
    print(comment)
    title = 'comments'
    return render_template('comment.html',title = title, comment = comment)

@main.route('/new_comment/<int:id>', methods = ['GET', 'POST'])
def new_comment(id):
    form = CommentForm()

    if form.validate_on_submit():
        writer = form.author.data
        com = form.comment.data

        new_comment = Comment(comment = com, blog_id = id, author= writer)
        new_comment.save_comment()

        return redirect(url_for('main.index'))

    title = 'New Comment'
    return render_template('new_comment.html', title = title, comment_form = form, pitch_id = id)

@main.route('/bloger/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    post = Blog.get_blog(user_id = current_user.id)
    print(post)

    title = uname

    return render_template('profile.html', user = user, blogs = post,title=title)