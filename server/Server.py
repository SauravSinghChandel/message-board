import bottle
from bottle import Bottle, route, request, template, redirect, response
from database_handler import DataBaseHandler
from beaker.middleware import SessionMiddleware
from ..HTML_Templates.Templates import *
from ..user_logic import *

hostName = "localhost"
serverPort = 8090

app = Bottle()

session_opts = {
        'session.cookie_expires': True
}

app = SessionMiddleware(app, session_opts)

@app.route('/login', method="GET"):
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

@app.route('/home')
def home():
    session = request.environ.get('beaker.session')
    return index.home(session)

@app.route('/logout')
def logout():
    session = request.environ.get('beaker.session')
    return logout.logout(session)


'''@app.route('/static/<filename>')
def server_static(self, filename):
    return bottle.static_file(filename, root='./static/')
'''

if __name__ == '__main__':
    bottle.run(app, host='localhost', port=8090)
