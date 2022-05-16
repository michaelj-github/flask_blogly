"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)

    first_name = db.Column(db.String(50),
                        nullable=False)

    last_name = db.Column(db.String(50),
                        nullable=False)

    image_url = db.Column(db.String(50), default="http://michaeljmurphy.com/Michael_J_Murphy.jpg")
    
class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    post_title = db.Column(db.String(60))

    post_content = db.Column(db.String(180))

    created_at = db.Column(db.String(26), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)

    tag_name = db.Column(db.String(50),
                        nullable=False)
