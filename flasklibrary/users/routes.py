from flask import Blueprint, render_template, url_for, flash, redirect, request
from flasklibrary import db, bcrypt
from flask_login import login_user, logout_user, current_user, login_required
from flasklibrary.models import User, Book
from flasklibrary.users.forms import RegistrationForm, LoginForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm

users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))

	form = RegistrationForm()

	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()

		flash("Account successfully created. Welcome, {}!".format(form.username.data), 'success')
		return redirect(url_for('main.home'))

	return render_template('register.html', title='Register', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))

	form = LoginForm()

	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()

		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('main.home'))
		else:
			flash('Unsuccessful Login. Please check username and password.', 'danger')

	return render_template('login.html', title='Login', form=form)


@users.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('main.home'))


@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
	form = UpdateAccountForm()

	if form.validate_on_submit():
		current_user.username = form.username.data
		current_user.email = form.email.data
		db.session.commit()
		flash('Your account has been successfully updated', 'success')
		return redirect(url_for('users.account'))

	elif request.method =='GET':
		form.username.data = current_user.username
		form.email.data = current_user.email

	return render_template('account.html', title='Account', form=form)


@users.route('/reset-password', methods=['GET', 'POST'])
def request_reset_password():
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))

	form =	RequestResetForm()

	return render_template('request_reset_password.html', title='Reset Password', form=form)
