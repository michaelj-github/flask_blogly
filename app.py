"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, Tag
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_db'
app.config['SECRET_KEY'] = "mjm34442"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
# db.create_all()

@app.route('/')
def home():
    """Home Page - Redirect to List of Users"""
    # users = User.query.all()
    return redirect("/users")

@app.route('/users')
def users():
    """List of Users"""
    users = User.query.all()
    tags = Tag.query.all()
    return render_template("home.html", users=users, tags=tags)

@app.route('/users/<int:user_id>')
def details(user_id):
    """Details Page - Details of a User"""
    user = User.query.get_or_404(user_id)
    posts = Post.query.filter_by(user_id = user.id)
    return render_template("details.html", user=user, posts=posts)    

@app.route('/users/new')
def create_view():
    """Create a User"""
    return render_template("create.html")        


@app.route('/users/new', methods=["POST"])
def create():
    """Create a User"""
    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    userURL = request.form["userURL"]
    new_user = User(first_name=firstname, last_name=lastname, image_url=userURL)
    db.session.add(new_user)
    db.session.commit()
    return redirect(f"/users/{new_user.id}")

@app.route('/users/<int:user_id>/edit')
def edit_view(user_id):
    """Edit View Details Page - View Details of a User for editing"""
    user = User.query.get_or_404(user_id)
    return render_template("edit.html", user=user)        

@app.route('/users/<int:user_id>/edit', methods=["POST"])
def edit(user_id):
    """Edit Details Page - Update Details of a User"""
    user = User.query.get(user_id)
    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    userURL = request.form["userURL"]
    user.first_name=firstname
    user.last_name=lastname
    user.image_url=userURL
    db.session.add(user)
    db.session.commit()
    return redirect(f"/users/{user.id}")

@app.route('/users/<int:user_id>/delete', methods=["POST"])
def delete(user_id):
    """Delete Page - Delete a User"""
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/users')

@app.route('/posts/<int:post_id>')
def post_details(post_id):
    """Details Page - Details of a post"""
    post = Post.query.get_or_404(post_id)
    user_id = post.user_id
    user = User.query.get_or_404(user_id)
    tags = Tag.query.all()
    return render_template("post_details.html", post=post, user_id=user_id, user=user, tags=tags) 

@app.route('/users/<int:user_id>/posts/new')
def post_create_view(user_id):
    """Create a Post"""
    user = User.query.get_or_404(user_id)
    tags = Tag.query.all()
    return render_template("post_create.html", user_id=user_id, tags=tags, user=user)        

@app.route('/users/<int:user_id>/posts/new', methods=["POST"])
def post_create(user_id):
    """Create a Post"""
    post_title = request.form["post_title"]
    post_content = request.form["post_content"]
    created_at = str(datetime.datetime.now())
    the_tags = [int(n) for n in request.form.getlist("thetags")]
    tags = Tag.query.filter(Tag.id.in_(the_tags)).all()
    new_post = Post(post_title=post_title, post_content=post_content, user_id=user_id, created_at=created_at, tags=tags)
    db.session.add(new_post)
    db.session.commit()
    return redirect(f"/users/{user_id}")

@app.route('/posts/<int:post_id>/edit')
def post_edit_view(post_id):
    """Edit View Post Details Page - View Details of a post for editing"""
    post = Post.query.get_or_404(post_id)
    user_id = post.user_id
    user = User.query.get_or_404(user_id)
    tags = Tag.query.all()
    return render_template("post_edit.html", post=post, user_id=user_id, tags=tags, user=user)        

@app.route('/posts/<int:post_id>/edit', methods=["POST"])
def post_edit(post_id):
    """Edit Post Details Page - Update Details of a Post"""
    post = Post.query.get(post_id)
    post_title = request.form["post_title"]
    post_content = request.form["post_content"]
    # created_at = post.created_at
    post.post_title=post_title
    post.post_content=post_content
    the_tags = [int(n) for n in request.form.getlist("thetags")]
    post.tags = Tag.query.filter(Tag.id.in_(the_tags)).all()
    db.session.add(post)
    db.session.commit()
    return redirect(f"/users/{post.user_id}")

@app.route('/posts/<int:post_id>/delete', methods=["POST"])
def post_delete(post_id):
    """Delete Post Page - Delete a Post"""
    post = Post.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(f"/users/{post.user_id}")

@app.route('/tags/<int:tag_id>')
def tag_details(tag_id):
    """Tag Details Page - Details of a Tag - just the name for now"""
    tag = Tag.query.get(tag_id)
    return render_template("tag_details.html", tag=tag)

@app.route('/tags/<tag_id>/delete', methods=["POST"])
def tag_delete(tag_id):
    """Delete tag Page - Delete a Tag"""
    tag = Tag.query.get(tag_id)
    db.session.delete(tag)
    db.session.commit()
    return redirect("/users")

@app.route('/tags/<tag_id>/edit')
def tag_edit_view(tag_id):
    """Edit View tag Details Page - View Details of a tag for editing"""
    tag = Tag.query.get(tag_id)
    return render_template("tag_edit.html", tag=tag)

@app.route('/tags/<tag_id>/edit', methods=["POST"])
def tag_edit(tag_id):
    """Edit tag Details Page - Update Details of a tag"""
    tag = Tag.query.get(tag_id)
    tag_name = request.form["tagname"]
    tag.tag_name = tag_name
    db.session.add(tag)
    db.session.commit()
    return redirect("/users")

@app.route('/tags/new')
def tag_create_view():
    """Create a tag"""
    return render_template("tag_create.html")

@app.route('/tags/new', methods=["POST"])
def tag_create():
    """Create a tag"""
    tagname = request.form["tagname"]
    new_tag = Tag(tag_name=tagname)
    db.session.add(new_tag)
    db.session.commit()
    return redirect("/users")


