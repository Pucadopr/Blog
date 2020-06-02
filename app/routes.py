from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', form=form)

@app.route('/')
@app.route('/index')
@login_required
def index(): 
    return render_template('Adminindex.html', title='Admin Panel', admin='admin')

@app.route('/categories')
def categories():
    return render_template('categories.html', title='Admin Panel', category='category')

@app.route('/details')
def details():
    return render_template('details.html', title='Admin Panel')

@app.route('/posts')
def posts():
    return render_template('posts.html', title='Admin Panel', post='post')

@app.route('/users')
def users():
    return render_template('users.html', title='Admin Panel', users='users')

@app.route('/profile')
def profile():
    return render_template('profile.html', title='Admin Panel')

@app.route('/settings')
def settings():
    return render_template('settings.html',title='Admin Panel')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# @app.route('/index')
# def index():
#     return render_template('index.html', title= 'Home')