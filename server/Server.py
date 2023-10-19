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


    @app.route('/signup', method='POST')


    def do_signup(self):
        username = request.forms.get('username')
        password = request.forms.get('password')

        result = db_handler.add((username, password))
        if result is not None:
            return result
        else:
            response.set_cookie('user', username)
            return redirect('/home')

    @app.route('/home')
    def home(self):
        username = request.get_cookie('user')
        if username:
            return f"Hello, {username}! Welcome to the home page."
        else:
            return redirect('/')

    @app.route('/logout')
    def logout(self):
        bottle.response.delete_cookie('user')
        return redirect('/')

    @app.route('/static/<filename>')
    def server_static(self, filename):
        return bottle.static_file(filename, root='./static/')


if __name__ == '__main__':
    bottle.run(app, host='localhost', port=8080)
