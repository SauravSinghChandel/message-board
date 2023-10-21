from bottle import request, redirect
from HTML_Templates.Templates import sign_in_page
from storage import dataHandler as dH
import secrets
import string
import hashlib
import os

dataHandler = dH.dataBaseHandler()

def encrypt_password(password, salt=None):
    if salt is None:
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')

    password_hash = hashlib.pbkdf2_hmac('sha256', password
                                        .encode('utf-8'), salt, 100000)

    salt = salt.hex()
    password_hash = password_hash.hex()

    return salt + password_hash


def is_user_id_unique(user_id):

    user_details = dataHandler.lookUpUserID(user_id)

    if len(user_details) == 0:
        return True

    return False


def generate_unique_user_id(length=12):

    alphabet = string.ascii_letters + string.digits

    while True:
        user_id = ''.join(secrets.choice(alphabet) for _ in range(length))
        if is_user_id_unique(user_id):
            return user_id


def username_available(username):
    user_details = dataHandler.lookUpUserName(username)
    if len(user_details) == 0:
        return True

    return False


def save_user(username, password):
    user_id = generate_unique_user_id()
    password_encrypted = encrypt_password(password)

    dataHandler.addUser((user_id, username, password_encrypted))


def signup_page():
    return sign_in_page.return_template()


def signup(session_data):
    username = request.forms.get('username')
    password = request.forms.get('password')
    retype_password = request.forms.get('retype-password')
    print('1')
    # Check if the password and retype_password match
    if password != retype_password:
        return "Password and retype password do not match. <a href='/signup'>Try again</a>"
    print('2')
    # Check if the username is already in use
    if not username_available(username):
        return "Username already in use. <a href='/signup'>Try a different username</a>"
    print(3)
    # Create the user
    save_user(username, password)
    print('4')
    # Set the user in the session
    session_data['user'] = username
    print(5)
    redirect('/')
