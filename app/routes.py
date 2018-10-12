from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask import request
from flask_login import current_user, login_user
from app.models import User
from app import db
from app.forms import LoginForm, ProjectPostForm, ExploreForm, RegistrationForm
from flask_login import current_user, login_required, logout_user
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Sam'}
    posts = [
            {
                'author': {'username': 'Cassie'},
                'body': 'Beautiful day in San Marcos!'
            },
            {
                'author': {'username': 'Brent'},
                'body': 'I enjoy machine learning!'
            }
        ]
    return render_template('index.html', title='Home', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/postnew', methods=['GET', 'POST'])
def postnew():
    form = ProjectPostForm()
    if form.validate():
        # post = Post(
        #     author=current_user,
        #     title=form.post.title,
        #     description=form.post.description,
        #     learned=form.post.learned,
        #     in_progress=form.post.in_progress,
        #     need_help=form.post.need_help,
        #     timestamp=form.post.timestamp
        # )
        # db.session.add(post)
        # db.session.commit()
        print('Author=', current_user)
        print('title=', form.post.title)
        print('etc...')
        return redirect(url_for('explore'))
    return render_template('postnew.html', title='Submit New Post',
        form=form)

@app.route('/explore', methods=['GET', 'POST'])
def explore():
    fakeposts = [
            {
                'title': 'Neural Network for Recognizing Handwritten Nums',
                'description': 'This project was a lot of fun!',
                'challenges': 'This was a really challenging project',
                'learned': 'We learned a LOT!',
                'in_progress': False,
                'need_help': None,
                'timestamp': '10-12-18 5:00pm'
            },
            {
                'title': 'Some Other Project',
                'description': 'This project was not so fun!',
                'challenges': None,
                'learned': None,
                'in_progress': True,
                'need_help': 'We need help in....',
                'timestamp': '10-11-18 3:00pm'
            }
        ]
    return render_template('explore.html', title='Explore', posts=fakeposts)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
