from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, ProjectPostForm, ExploreForm
from flask_login import current_user, LoginManager

@app.route('/')
@app.route('/index')
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
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me{}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
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


