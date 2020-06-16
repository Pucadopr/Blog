from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, AddUserForm, CategoryForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Category, Post
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

@app.route('/index', methods=['GET', 'POST'])
@login_required
def index(): 
    userform = AddUserForm()
    categoryform = CategoryForm()
    if userform.validate_on_submit():
        user = User(name=userform.name.data, email=userform.email.data)
        user.set_password(userform.password.data)
        db.session.add(user)
        db.session.commit()
        flash('User registration successful')
        return redirect(url_for('index'))
    
    if categoryform.validate_on_submit():
        cat = Category(title=categoryform.title.data)
        db.session.add(cat)
        db.session.commit()
        flash('New Category added successful')
        return redirect(url_for('index'))

    totalusers= db.session.query(User).count()
    totalcategory= db.session.query(Category).count()
    totalposts= db.session.query(Post).count()

    return render_template('Adminindex.html', title='Admin Panel', admin='admin', userform=userform, categoryform= categoryform, totalusers=totalusers, totalcategory= totalcategory, totalposts= totalposts)

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

@app.route('/')
def home_page():
    return render_template('single.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

#  