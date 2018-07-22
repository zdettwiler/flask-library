from flask import url_for
from flasklibrary import mail
from flask_mail import Message


def send_reset_email(user):
	token = user.create_reset_token()
	msg = Message('Password Reset Request',
					sender='noreply@demo.com',
					recipients=[user.email])

	msg.body = '''Click on the following link to reset your password: {}'''.format(url_for('users.reset_password', token=token, _external=True))

	mail.send(msg)
