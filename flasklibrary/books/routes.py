from flask import Blueprint, render_template, url_for, flash, redirect, request
from flasklibrary import db
from flask_login import current_user, login_required
from flasklibrary.models import User, Book
from flasklibrary.books.forms import BookForm

books = Blueprint('books', __name__)

@books.route('/book/<int:book_id>')
def book(book_id):
	book = Book.query.get_or_404(book_id)

	return render_template('book.html', title=book.title, book=book)


@books.route('/book/add', methods=['GET', 'POST'])
@login_required
def add_book():
	form = BookForm()

	if form.validate_on_submit():
		book = Book(title=form.title.data, author=form.author.data, category=form.category.data)
		db.session.add(book)
		db.session.commit()

		flash('Your book has been added to the library!', 'success')
		return redirect(url_for('main.home'))

	return render_template('add_book.html', title="Add a Book", form=form)


@books.route('/book/<int:book_id>/update', methods=['GET', 'POST'])
@login_required
def update_book(book_id):
	book = Book.query.get_or_404(book_id)
	form = BookForm()

	if form.validate_on_submit():
		book.title = form.title.data
		book.author = form.author.data
		book.category = form.category.data
		db.session.commit()
		flash('Your book has been updated!', 'success')
		return redirect(url_for('books.book', book_id=book.id))

	elif request.method == 'GET':
		form.title.data = book.title
		form.author.data = book.author
		form.category.data = book.category
		# form.read.data = book.read

	return render_template('update_book.html', title="Update a Book", book=book, form=form)

@books.route('/book/<int:book_id>/delete', methods=['POST'])
@login_required
def delete_book(book_id):
	book = Book.query.get_or_404(book_id)
	db.session.delete(book)
	db.session.commit()

	flash('Your book has been deleted!', 'success')
	return redirect(url_for('main.home'))
