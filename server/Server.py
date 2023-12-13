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

@app.route('/login', method="GET")
def login_page():
    return login.login_page()

'''Calling login_page function from user_logic login.py
Using GET method here.'''

@app.route('/login', method='POST')
def do_login():
    session = request.environ.get('beaker.session')
    return login.do_login(session)

'''Calling do_login function from user_logic login.py
Using POST method here and passing a session ID'''

@app.route('/signup', method='GET')
def signup_page():
    return signin.signup_page()

'''Calling signup_page function from user_logic signin.py
Using GET method here.'''

@app.route('/signup', method='POST')
def signup():
    session = request.environ.get('beaker.session')
    return signin.signup(session)


'''Calling signup function from user_logic signin.py
Using POST method here and passing a session ID'''

@app.route('/')
def home():
    session = request.environ.get('beaker.session')
    return session_check.index(session)

'''Calling index function from user_logic session_check.py
passing a session ID'''

@app.route('/logout')
def logout():
    session = request.environ.get('beaker.session')
    return login.logout(session)

'''Calling logout function from user_logic login.py
passing a session ID'''

@app.route('/post', method="POST")
def add_post():
    session = request.environ.get('beaker.session')
    return post.make_post(session)

'''Calling make_post function from logic post.py
Using POST method here and passing a session ID'''

@app.route('/search', method="POST")
def search_results():
    session = request.environ.get('beaker.session')
    return search.return_search_page()

'''Calling return_search_page function from logic search.py
Using POST method here and passing a session ID'''

@app.route('/like/<message_id>', method="POST")
def like_message(message_id):
    session = request.get('beaker.session')
    return ratings.like(session, message_id)

'''Calling like function from logic ratings.py
Using POST method here and passing a session ID'''

@app.route('/dislike/<message_id>', method="POST")
def dislike_message(message_id):
    session = request.get('beaker.session')
    return ratings.dislike(session, message_id)

'''Calling dislike function from logic ratings.py
Using POST method here and passing a session ID'''

@app.route('/structure/<message_id>', method="POST")
def structure_message(message_id):
    session = request.get('beaker.session')
    return ratings.structure(session, message_id)

'''Calling structure function from logic ratings.py
Using POST method here and passing a session ID'''

@app.route('/quality/<message_id>', method="POST")
def quality_message(message_id):
    session = request.get('beaker.session')
    return ratings.quality(session, message_id)

'''Calling quality function from logic ratings.py
Using POST method here and passing a session ID'''

@app.route('/editUsername', method='GET')
def ch_uname_page():
    return ch_uname.returnTemplate()

'''Calling returnTemplate function from user_logic ch_uname.py
Using GET method here and passing a session ID'''

@app.route('/editPassword', method='GET')
def ch_uname_page():
    return ch_pass.returnTemplate()

'''Calling returnTemplate function from user_logic ch_pass.py
Using GET method here and passing a session ID'''

@app.route('/changeUsername', method='POST')
def ch_uname_page():
    session = request.get('beaker.session')
    return ch_uname.changeUsername(session)

'''Calling changeUsername function from user_logic ch_uname.py
Using POST method here and passing a session ID'''

@app.route('/changePassword', method='POST')
def ch_uname_page():
    session = request.get('beaker.session')
    return ch_pass.changePassword(session)

'''Calling changePassword function from user_logic ch_pass.py
Using POST method here and passing a session ID'''

app = SessionMiddleware(app, session_opts)


def run():
    bottle.run(app, host='localhost', port=8090)