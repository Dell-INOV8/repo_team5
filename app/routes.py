from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask import request
from flask_login import current_user, login_user
from app.models import User, Post
from app import db
from app.forms import LoginForm, ProjectPostForm, ExploreForm, RegistrationForm
from flask_login import current_user, login_required, logout_user
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
def index():
    return redirect(url_for('explore'))

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
    if form.validate_on_submit():
        post = Post(
            author=current_user,
            title=form.title,
            description=form.description,
            learned=form.learned,
            in_progress=form.in_progress,
            challenges=form.challenges,
            need_help=form.need_help,
            timestamp=form.timestamp
        )
        db.session.add(post)
        db.session.commit()
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
