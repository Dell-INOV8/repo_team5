from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

interest_identifier = db.Table('interest_identifier', db.Model.metadata,
	db.Column('user_id', db.Integer, db.ForeignKey('users.user_id')),
	db.Column('interest_id', db.Integer, db.ForeignKey('interests.interest_id'))
)

class User(db.Model):
	__tablename__ = 'users'
	user_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	projects = db.relationship('Post', backref='author', lazy='dynamic')
	interests = db.relationship('Interest', secondary=interest_identifier)

	def __repr__(self):
		return '<User {}>'.format(self.username)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)
	

class Post(db.Model):
	post_id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100))
	description = db.Column(db.String(300))
	challenges = db.Column(db.String(300))
	learned = db.Column(db.String(300))
	need_help = db.Column(db.String(300))
	in_progress = db.Column(db.Boolean)
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

	def __repr__(self):
		return '<Project {}>'.format(self.name)


class Interest(db.Model):
	__tablename__ = 'interests'
	interest_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), index=True, unique=True)
	#users = db.relationship('Interest', secondary=association_table)
