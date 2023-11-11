import bottle
from bottle import Bottle, route, request, response
from storage import dataHandler
from beaker.middleware import SessionMiddleware
from logic import post, search
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

'''Calling login_page method from user_logic, login.py
Using GET method here.'''

@app.route('/login', method="GET")
def login_page():
    return login.login_page()

'''Calling do_login method from user_logic, login.py
Using POST method here and passing a session ID'''

@app.route('/login', method='POST')
def do_login():
    session = request.environ.get('beaker.session')
    return login.do_login(session)

'''Calling signin method from user_logic, signin.py
Using GET method here.'''

@app.route('/signup', method='GET')
def signup_page():
    return signin.signup_page()

'''Calling signin method from user_logic, signin.py
Using POST method here and passing a session ID'''

@app.route('/signup', method='POST')
def signup():
    session = request.environ.get('beaker.session')
    return signin.signup(session)

'''Calling home method from user_logic, session_check.py
passing a session ID'''

@app.route('/')
def home():
    session = request.environ.get('beaker.session')
    return session_check.index(session)

'''Calling logout method from user_logic, login.py
passing a session ID'''

@app.route('/logout')
def logout():
    session = request.environ.get('beaker.session')
    return login.logout(session)

'''Calling make_post method from logic, post.py
Using POST method here and passing a session ID'''

@app.route('/post', method="POST")
def add_post():
    session = request.environ.get('beaker.session')
    return post.make_post(session)


'''Calling return_search_users method from logic, search.py
Using POST method here and passing a session ID'''

@app.route('/search', method="POST")
def search_results():
    session = request.environ.get('beaker.session')
    return search.return_search_page()

app = SessionMiddleware(app, session_opts)

def run():
    bottle.run(app, host='localhost', port=8090)