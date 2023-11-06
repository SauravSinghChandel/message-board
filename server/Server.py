import bottle
from bottle import Bottle, route, request, response
from storage import dataHandler
from dataHandler import *
from beaker.middleware import SessionMiddleware
from logic import post
from user_logic import login, session_check, signin
import sys

sys.path.append("..")
hostName = "localhost"
serverPort = 8090

app = Bottle()

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': True,
    'session.data_dir': './session_data',
    'session.auto': True
}


@app.route('/login', method="GET")
def login_page():
    return login.login_page()

'''Calling login_page function from user_logic, authenication login.py
Using GET method here.'''

@app.route('/login', method='POST')
def do_login():
    session = request.environ.get('beaker.session')
    return login.do_login(session)

'''Calling do_login function from user_logic, authenication login.py
Using POST method here and passing a session ID'''

@app.route('/signup', method='GET')
def signup_page():
    return signin.signup_page()

'''Calling signin function from user_logic, authenication signin.py
Using GET method here.'''

@app.route('/signup', method='POST')
def signup():
    session = request.environ.get('beaker.session')
    return signin.signup(session)


'''Calling signin function from user_logic, authenication signin.py
Using POST method here and passing a session ID'''
@app.route('/')
def home():
    session = request.environ.get('beaker.session')
    return session_check.index(session)

'''Calling home function from user_logic, authenication session_check.py
passing a session ID'''

@app.route('/logout')
def logout():
    session = request.environ.get('beaker.session')
    return login.logout(session)

@app.route('/post', method="POST")
def add_post():
    session = request.environ.get('beaker.session')
    return post.make_post(session)

'''Looking up the user by username from the database '''

@app.route('/search', method="POST")
def search():
    name = request.form['userName']
    # Use the imported function from dataHandler to look up the user by name
    user_info = lookUpUserByName(name)
    if user_info:
        return f"User found: {user_info}"
    else:
        return "User not found."

@app.route('/search', method="GET")
def search():
    name = request.form['userName']
    # Use the imported function from dataHandler to look up the user by name
    user_info = lookUpUserByName(name)
    if user_info:
        return f"User found: {user_info}"
    else:
        return "User not found."

@app.route('/search', method="POST")
def search():
    pass

@app.route('/search', method="GET")
def search():
    pass

app = SessionMiddleware(app, session_opts)

def run():
    bottle.run(app, host='localhost', port=8090)
