from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
	TextAreaField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')

class ExploreForm(FlaskForm):
	submit_new = SubmitField('Submit New Post')

class ProjectPostForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired(),
		Length(min=10, max=100)])
	in_progress = BooleanField('Is the project still in progress?')
	description = TextAreaField('Description', validators=[
        DataRequired(), Length(min=10, max=300)])
	need_help = TextAreaField('Need Help')
	challenges = TextAreaField('Challenges')
	learned = TextAreaField('What I Learned')
	submit = SubmitField('Submit New Post')

	