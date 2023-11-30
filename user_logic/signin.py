from bottle import request, redirect
from HTML_Templates.Templates import sign_in_page
from storage import dataHandler as dH
import secrets
import string
from cryptography.fernet import Fernet

key = b'2hX8MUwJ_JDcuQTv2YnwsVcP7Bij3Bw_9KTFkvhDiMc='
fernet = Fernet(key)
dataHandler = dH.dataBaseHandler()




def is_user_id_unique(user_id):
    """
    Check if a user ID is unique in the database.

    Args:
        user_id (str): The user ID to be checked.

    Returns:
        bool: True if the user ID is unique; False if it already exists in the database.
    """
    user_details = dataHandler.lookUpUserID(user_id)

    if len(user_details) == 0:
        return True

    return False


def generate_unique_user_id(length=12):
    """
    Generate a unique user ID of the specified length.

    Args:
        length (int, optional): The length of the user ID to be generated. Default is 12.

    Returns:
        str: A unique user ID.
    """
    alphabet = string.ascii_letters + string.digits

    while True:
        user_id = ''.join(secrets.choice(alphabet) for _ in range(length))
        if is_user_id_unique(user_id):
            return user_id


def username_available(username):
    """
    Check if a username is available (not already in use).

    Args:
        username (str): The username to be checked.

    Returns:
        bool: True if the username is available; False if it is already in use.
    """
    user_details = dataHandler.lookUpUserName(username)
    if len(user_details) == 0:
        return True

    return False


def save_user(username, password):
    """
    Save a new user with a unique user ID and an encrypted password.

    Args:
        username (str): The username of the new user.
        password (str): The unencrypted password of the new user.

    Returns:
        None
    """
    user_id = generate_unique_user_id()
    password_encrypted = fernet.encrypt(password.encode())

    dataHandler.addUser((user_id, username, password_encrypted))


def signup_page():
    """
    Return the HTML template for the sign-up page.

    Returns:
        str: HTML template for the sign-up page.
    """
    return sign_in_page.return_template()


def signup(session_data):
    """
    Process user sign-up, including password validation, username availability, and user creation.

    Args:
        session_data (dict): The user's session data for session management.

    Returns:
        str or None: If sign-up is successful, returns None and redirects to the home page.
                     If sign-up fails, returns an error message with a link to try again.
    """
    username = request.forms.get('username')
    password = request.forms.get('password')
    retype_password = request.forms.get('retype-password')
    # Check if the password and retype_password match
    if password != retype_password:
        return "Password and retype password do not match. <a href='/signup'>Try again</a>"
    # Check if the username is already in use
    if not username_available(username):
        return "Username already in use. <a href='/signup'>Try a different username</a>"
    # Create the user
    save_user(username, password)
    # Set the user in the session
    session_data['user'] = username
    redirect('/')
