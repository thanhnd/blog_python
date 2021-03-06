from flask import render_template, flash, redirect, g, session
from app import app
from .forms import LoginForm, RegisterForm, CreatePostForm
from .models import database, User, Post

app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'

@app.before_request
def before_request():
    # Do connect database
    g.db = database
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.route('/')
@app.route('/index')
def index():
    posts = Post.select()
    return render_template("index.html", posts = posts)

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = User.get(email = form.email.data, password = form.password.data)
            session['user_email'] = user.email
            session['user_id'] = user.id
            flash('Login Success with id= %s' % session['user_id'])
            return redirect('/index')
        except User.DoesNotExist:
            flash('Login Fail for email= %s, password=%s, remember_me=%s' %
                (form.email.data, form.password.data, str(form.remember_me.data)))

    return render_template('login.html',
            title = 'Sign In',
            form = form)

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.create(email = form.email.data, password = form.password.data)
        user.save();
        flash('Resgister succesfully, welcome')
        return redirect('/index')
    return render_template('register.html',
            title = 'Register',
            form = form)

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

@app.route('/posts/create', methods=['POST', 'GET'])
def create_post():
    form = CreatePostForm()
    if form.validate_on_submit():

        try:
            user = User.get(id = session['user_id'])
            post = Post.create(title = form.title.data,
                content = form.content.data,
                author = user)
            post.save()
            flash('Create post %s succesfully.' % post.title)
            return redirect('/index')
        except User.DoesNotExist:
            flash('Login Fail for email= %s, password=%s, remember_me=%s' %
                (form.email.data, form.password.data, str(form.remember_me.data)))

    return render_template('post/create.html',
            title = 'Create post',
            form = form)

@app.route('/posts/')
def show_posts():
    # Show the user profile for that user
    return 'Post %d' % post_id
