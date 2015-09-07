from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname' : 'Thanh Nguyen'}
    posts = [
        {
            'author': {'nickname' : 'Ha'},
            'body': "Life of Pi"
        },
        {
            'author': {'nickname' : 'Linh'},
            'body': "Adventure"
        }
    ]
    return render_template("index.html",
            user = user,
            posts = posts)

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID= %s, remember_me=%s' %
            (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
            title = 'Sign In',
            form = form,
            providers = app.config['OPENID_PROVIDERS'])

@app.route('/hello')
def hello():
    return render_template("index.html", foo_string="Hello Template")

@app.route('/users/<username>')
def show_user_profile(username):
    # Show the user profile for that user
    return 'User %s' % username

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    # Show the user profile for that user
    return 'Post %d' % post_id

@app.route('/posts/')
def show_posts():
    # Show the user profile for that user
    return 'Post %d' % post_id
