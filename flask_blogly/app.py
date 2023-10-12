"""Blogly application."""

from flask import Flask, render_template, request, redirect
from models import db, connect_db, User
#from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:SmokingPot420@localhost/blogly_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

#toolbar = DebugToolbarExtension(app)

connect_db(app)
app.app_context().push()
db.create_all()

#from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
#debug = DebugToolbarExtension(app)


@app.route('/')
def root():
    """ Homepage redirects to list of users. """

    return redirect("/users")



##########################################################
@app.route('/users')
def users_index():
    """Show a page with info on all users"""

    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('users/index.html', users=users)

@app.route('/users/new', methods=["GET"])
def users_new_form():
    """ Show a form to create a new user. """
    return render_template('users/new.html')

@app.route("/users/new", methods=["GET", "POST"])
def add_user():
    """ Handle form submission for creating a new user """

    new_user = User(
        first_name=request.form['first_name'], 
        last_name=request.form['last_name'], 
        image_url=request.form['image_url'])
    
    db.session.add(new_user)
    db.session.commit()

    return redirect("/users")

@app.route("/users/<int:user_id>")
def show_user(user_id):
    """Show info on specific user."""

    user = User.query.get_or_404(user_id)
    return render_template("users/show.html", user=user)

@app.route('/users/<int:user_id>/edit') 
def users_edit(user_id):
    """ Show a form to edit an existing user """

    user = User.query.get_or_404(user_id)
    return render_template('users/edit.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def users_update(user_id):
    """ Handle form submission for ubdating an existing user """

    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def users_delete(user_id):
    """ Handle form submission for deleting an existing user """

    user= User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect('/users')