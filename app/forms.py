from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
	TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User

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

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
            'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
            
        
