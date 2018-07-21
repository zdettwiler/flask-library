from flasklibrary import db, login_manager
from flask_login import UserMixin
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(100), unique=True, nullable=False)
	avatar = db.Column(db.String(20), nullable=False, default='default_avatar.png')
	password = db.Column(db.String(60), nullable=False)
	#read_books = db.relationship('Book', backref='read', lazy=True)

	def __repr__(self):
		return "<User{} {} email='{}'>".format(self.id, self.username, self.email)

class Book(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(200), nullable=False)
	author = db.Column(db.String(100), unique=True, nullable=False)
	cover = db.Column(db.String(20), nullable=False, default='default_cover.jpg')
	category = db.Column(db.String(20))
	#read_by_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return "<Book{} {}>".format(self.id, self.title)
