from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flasklibrary.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app)
	login_manager.login_view = 'users.login'
	login_manager.login_message_category = 'info'

	from flasklibrary.main.routes import main
	from flasklibrary.users.routes import users
	from flasklibrary.books.routes import books
	app.register_blueprint(main)
	app.register_blueprint(users)
	app.register_blueprint(books)

	return app
