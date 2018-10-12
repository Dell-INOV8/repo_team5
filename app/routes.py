from flask import render_template
from app import app

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

