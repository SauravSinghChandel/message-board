import bottle
from bottle import Bottle, route, request, template, redirect, response
from database_handler import DataBaseHandler

hostName = "localhost"
serverPort = 8090

app = Bottle()

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.app = Bottle()
        self.db_handler = DataBaseHandler()

    @app.route('/')
    def login(self):
        return template('login')

    @app.route('/login', method='POST')
    def do_login(self):
        username = request.forms.get('username')
        password = request.forms.get('password')

        # Check if the user exists
        user_info = db_handler.lookUpUserName(username)
        if user_info and user_info[2] == password:
            response.set_cookie('user', username)
            return redirect('/home')
        else:
            return "Login failed. Invalid username or password."

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
