"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

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
    return render_template("home.html", users=users)

@app.route('/users/<int:user_id>')
def details(user_id):
    """Details Page - Details of a User"""
    user = User.query.get_or_404(user_id)
    return render_template("details.html", user=user)    

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

