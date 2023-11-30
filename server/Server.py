import sys
sys.path.append("../")
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

@app.route('/message/<message_id>/<user_id>')
def message():
    message_id = request
    user_id = request
    return f"The Message Id for this message is: {message_id} from User Id : {user_id}"

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

@app.route('/search', method="POST")
def search_results():
    session = request.environ.get('beaker.session')
    return search.return_search_page()

app = SessionMiddleware(app, session_opts)


def run():
    bottle.run(app, host='localhost', port=8090)