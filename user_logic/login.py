from bottle import request, redirect
from storage import dataHandler as dH
from HTML_Templates.Templates import login_page as lp
import hashlib

dataHandler = dH.dataBaseHandler()


def verify_password(stored_password, provided_password):   
    """
    Verify a user's password by comparing the provided password with the stored password hash.

    Args:
        stored_password (str): The stored password hash, which includes the salt.
        provided_password (str): The password provided by the user for authentication.

    Returns:
        bool: True if the provided password matches the stored password; False otherwise.
    """
    salt = stored_password[:64]  # The first 64 characters are the salt
    stored_password = stored_password[64:]  # The rest is the hashed password

    password_hash = hashlib.pbkdf2_hmac('sha256', provided_password
                                        .encode('utf-8'),
                                        salt.encode('ascii'), 100000)
    password_hash = password_hash.hex()

    return password_hash == stored_password


def login_page():
    """
    Return the HTML template for the login page.

    Returns:
        str: HTML template for the login page.
    """
    return lp.return_template()


def login(username, password):
    """
    Authenticate a user based on their username and password.

    Args:
        username (str): The username provided by the user.
        password (str): The password provided by the user for authentication.

    Returns:
        bool: True if the user is authenticated; False otherwise.
    """
    user_details = dataHandler.lookUpUserName(username)
    if len(user_details) == 1:
        user_details = list(user_details[0])
        if username == user_details[1] and verify_password(password, user_details[2]):
            print('true')
            return True

    return False


def do_login(session_data):
    """
    Process user login and session management.

    Args:
        session_data (dict): The user's session data for session management.

    Returns:
        str or None: If login is successful, returns None and redirects to the home page.
                     If login fails, returns an error message with a link to try again.
    """
    username = request.forms.get('username')
    password = request.forms.get('password')
    if login(username, password):
        session_data['user'] == username
        redirect('/')
    else:
        return "Login failed. <a href='/login'>Try again</a>"


def logout(session_data):
    """
    Log out the user by removing their session data.

    Args:
        session_data (dict): The user's session data for session management.

    Returns:
        None
    """
    session_data.pop('user', None)
    redirect('/')
