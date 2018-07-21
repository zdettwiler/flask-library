from flask import Blueprint, render_template
from flasklibrary.models import Book

main = Blueprint('main', __name__)

@main.route("/")
def home():
	books = Book.query.all()
	return render_template('home.html', title="Home", books=books)

@main.route("/about")
def about():
	return render_template('about.html', title="About")
