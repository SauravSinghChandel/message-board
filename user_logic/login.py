from bottle import request, redirect
from storage import dataHandler as dH
from HTML_Templates.Templates import login_page as lp
import hashlib

dataHandler = dH.dataBaseHandler()


def verify_password(stored_password, provided_password):
    salt = stored_password[:64]  # The first 64 characters are the salt
    stored_password = stored_password[64:]  # The rest is the hashed password

    password_hash = hashlib.pbkdf2_hmac('sha256', provided_password
                                        .encode('utf-8'),
                                        salt.encode('ascii'), 100000)
    password_hash = password_hash.hex()

    return password_hash == stored_password


def login_page():
    return lp.return_template()


def login(username, password):

    user_details = dataHandler.lookUpUserName(username)
    if len(user_details) == 1:
        user_details = list(user_details[0])
        if username == user_details[1] and verify_password(password, user_details[2]):
            print('true')
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
