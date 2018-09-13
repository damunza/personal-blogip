from flask_login import UserMixin
from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash

class User(UserMixin,db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    blog = db.relationship('Blog', backref = 'username', lazy = 'dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f' {self.username}'

class Blog(db.Model):

    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key = True)
    blog = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def delete_blog(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_blog(cls, user_id):
        blog = Blog.query.filter_by(id=user_id).all()
        return blog


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))