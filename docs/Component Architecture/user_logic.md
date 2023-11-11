# User Logic: 
This module all the code affecting and mainting user and 
### login.py : 
Imports:

The code imports necessary modules such as request, redirect, login_page template, dataHandler from storage, hashlib, and cryptography-related modules (Fernet).
Global Variables:

dataHandler: An instance of the dataBaseHandler class from the storage module.
key: A byte string used as the key for Fernet encryption.
fernet: An instance of the Fernet class using the provided key.
Functions:

verify_password(stored_password, provided_password):

Verifies a user's password by comparing the provided password with the stored password hash.
Decrypts the stored password using Fernet before comparison.
Returns True if the provided password matches the stored password; False otherwise.
login_page():

Returns the HTML template for the login page using lp.return_template().
login(username, password):

Authenticates a user based on their username and password.
Retrieves user details from the database, and if a match is found, verifies the password using verify_password.
Returns True if the user is authenticated; False otherwise.
do_login(session_data):

Processes user login and session management:
Retrieves the username and password from the login form.
Calls login to authenticate the user.
If successful, sets the user in the session and redirects to the home page.
If login fails, returns an error message with a link to try again.
logout(session_data):

Logs out the user by removing their session data.
Redirects to the home page.
Workflow:

The do_login function is likely called when a user submits a login form.
It retrieves user input, authenticates the user using login, and sets the user in the session if successful.
The logout function is called when a user requests to log out, removing their session data.
Error Handling:

The code handles login failures by providing an error message with a link to try again.
Security:

Passwords are stored as encrypted hashes in the database using Fernet.
The code uses a secure method for password verification (verify_password) by decrypting and comparing.
HTML Templates:

The login_page function returns the HTML template for the login page.

### signin.py :
Imports:

The code imports necessary modules such as request, redirect, sign_in_page template, dataHandler from storage, and cryptography-related modules (secrets and Fernet).
Global Variables:

key: A byte string used as the key for Fernet encryption.
fernet: An instance of the Fernet class using the provided key.
dataHandler: An instance of the dataBaseHandler class from the storage module.
Functions:

is_user_id_unique(user_id):

Checks if a user ID is unique in the database.
Returns True if the user ID is unique; False if it already exists in the database.
generate_unique_user_id(length=12):

Generates a unique user ID of the specified length.
Uses the secrets module to create a random ID until a unique one is found.
username_available(username):

Checks if a username is available (not already in use).
Returns True if the username is available; False if it is already in use.
save_user(username, password):

Saves a new user with a unique user ID and an encrypted password.
Generates a unique user ID using generate_unique_user_id.
Encrypts the password using Fernet before saving it to the database.
signup_page():

Returns the HTML template for the sign-up page using sign_in_page.return_template().
signup(session_data):

Processes user sign-up:
Validates password and retype-password match.
Checks if the username is available.
Creates the user and saves the information.
Sets the user in the session.
Redirects to the home page if successful.
Returns an error message with a link to try again if unsuccessful.
Workflow:

The signup function is likely called when a user submits a sign-up form.
It validates user input, checks for username availability, and creates a new user.
The user is then set in the session, and the user is redirected to the home page.
Error Handling:

The code performs basic error handling, such as checking if the password and retype-password match and if the username is available.
HTML Templates:

The signup_page function returns the HTML template for the sign-up page.
Security:

Passwords are encrypted before being stored in the database using Fernet.

### session_check.py : 
HTML Templates (home_page and login_page):

These templates are assumed to be responsible for generating HTML content for the home page and login page, respectively.
Logic (index function):

Responsibility:
Displays the appropriate page (home page or login page) based on the user's session status.
Components:
Home Page:
Generated using home_page.return_template when the user is logged in.
Login Page:
Generated using login_page.return_template when the user is not logged in.
Interactions:
Communicates with the HTML template functions to generate the appropriate HTML content.
Input:
session_data (dict): The user's session data for session management.
Output:
HTML template for the home page if the user is logged in.
HTML template for the login page if the user is not logged in.
Session Data:

Assumed to be a dictionary containing information about the user's session.
Used to determine whether the user is logged in.
Web Application Flow:

The index function serves as an entry point for rendering pages based on the user's session status.
If the 'user' key is present in session_data, it returns the home page; otherwise, it returns the login page.
User Authentication:

Assumes that the presence of the 'user' key in the session_data dictionary indicates that the user is logged in.
External Dependencies:

Depends on external modules (HTML_Templates.Templates) for HTML template generation.