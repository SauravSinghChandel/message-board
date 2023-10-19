from bottle import request, redirect
from ..storage import dataHandler
from ..HTML_Templates.Templates import *
import hashlib


def verify_password(stored_password, provided_password):
    salt = stored_password[:64]  # The first 64 characters are the salt
    stored_password = stored_password[64:]  # The rest is the hashed password

    password_hash = hashlib.pbkdf2_hmac('sha256', provided_password
                                        .encode('utf-8'),
                                        salt.encode('ascii'), 100000)
    password_hash = password_hash.hex()

    return password_hash == stored_password


def login_page():
    return login_page.return_template()

def login(username, password):

    user_details = dataHandler.lookupUserName(username)

    if username == user_details[1] and verify_password(password, user_details[2]):
        return True

    return False


def do_login(session_data):
    username = request.forms.get('username')
    password = request.forms.get('password')

    if login(username, password):
        session_data['user'] == username
        redirect('/')
    else:
        return "Login failed. <a href='/login'>Try again</a>"


def logout(session_data):
    session_data.pop('user', None)
    redirect('/')
