import sys
sys.path.append("../")
import bottle
from bottle import Bottle, route, request, response
from storage import dataHandler
from beaker.middleware import SessionMiddleware
from logic import post, search, ratings
from user_logic import login, session_check, signin, ch_uname, ch_pass
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

@app.route('/like/<message_id>', method="POST")
def like_message(message_id):
    session = request.get('beaker.session')
    return ratings.like(session, message_id)

@app.route('/dislike/<message_id>', method="POST")
def dislike_message(message_id):
    session = request.get('beaker.session')
    return ratings.dislike(session, message_id)

@app.route('/structure/<message_id>', method="POST")
def strucutre_message(message_id):
    session = request.get('beaker.session')
    return ratings.structure(session, message_id)

@app.route('/quality/<message_id>', method="POST")
def quality_message(message_id):
    session = request.get('beaker.session')
    return ratings.quality(session, message_id)

@app.route('/editUsername', method='GET')
def ch_uname_page():
    return ch_uname.returnTemplate()

@app.route('/editPassword', method='GET')
def ch_uname_page():
    return ch_pass.returnTemplate()
    
@app.route('/changeUsername', method='POST')
def ch_uname_page():
    session = request.get('beaker.session')
    return ch_uname.changeUsername(session)

@app.route('/changePassword', method='POST')
def ch_uname_page():
    session = request.get('beaker.session')
    return ch_pass.changePassword(session)

app = SessionMiddleware(app, session_opts)


def run():
    bottle.run(app, host='localhost', port=8090)