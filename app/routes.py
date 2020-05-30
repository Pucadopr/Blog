from flask import render_template
from app import app

user = {'username': 'Pucado'}

@app.route('/')
@app.route('/index')
def index():
    
    return render_template('Adminindex.html', title='Admin Panel', user=user)

@app.route('/categories')
def categories():
    return render_template('categories.html', title='Admin Panel', user=user)

@app.route('/details')
def details():
    return render_template('details.html', title='Admin Panel', user=user)

@app.route('/posts')
def posts():
    return render_template('posts.html', title='Admin Panel', user=user)

@app.route('/users')
def users():
    return render_template('users.html', title='Admin Panel', user=user)

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