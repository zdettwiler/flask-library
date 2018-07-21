from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flasklibrary.models import User

class BookForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired(), Length(min=2, max=200)])
	author = StringField('Author', validators=[DataRequired()])
	category = StringField('Category', validators=[DataRequired()])
	read = BooleanField("I've read the book.")
	submit = SubmitField('Add Book')
