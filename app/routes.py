from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

user = {'username': 'Pucado'}

@app.route('/login', methods=['GET', 'POST'])
def login():
    form= LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.email.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/')
@app.route('/index')
def index(): 
    return render_template('Adminindex.html', title='Admin Panel', user=user, admin='admin')

@app.route('/categories')
def categories():
    return render_template('categories.html', title='Admin Panel', user=user, category='category')

@app.route('/details')
def details():
    return render_template('details.html', title='Admin Panel', user=user)

@app.route('/posts')
def posts():
    return render_template('posts.html', title='Admin Panel', user=user, post='post')

@app.route('/users')
def users():
    return render_template('users.html', title='Admin Panel', user=user, users='users')

@app.route('/profile')
def profile():
    return render_template('profile.html', title='Admin Panel', user=user)

@app.route('/settings')
def settings():
    return render_template('settings.html',title='Admin Panel', user=user)

@app.route('/logout')
def logout():
    return render_template('settings.html', title='Admin Panel', user=user)


# @app.route('/index')
# def index():
#     return render_template('index.html', title= 'Home')