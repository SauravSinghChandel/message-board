import bottle
from bottle import Bottle, route, request, response
from storage import dataHandler
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

@app.route('/login', method='POST')
def do_login():
    session = request.environ.get('beaker.session')
    return login.do_login(session)

@app.route('/signup', method='GET')
def signup_page():
    return signin.signup_page()

@app.route('/signup', method='POST')
def signup():
    session = request.environ.get('beaker.session')
    return signin.signup(session)

@app.route('/')
def home():
    session = request.environ.get('beaker.session')
    return session_check.index(session)

@app.route('/logout')
def logout():
    session = request.environ.get('beaker.session')
    return login.logout(session)

@app.route('/post', method="POST")
def add_post():
    session = request.environ.get('beaker.session')
    return post.make_post(session)

app = SessionMiddleware(app, session_opts)

def run():
    bottle.run(app, host='localhost', port=8090)
