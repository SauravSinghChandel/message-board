from bottle import Bottle, request, response, redirect
import sys

import ctypes  # An included library with Python install.

"""
Sign in page
Username Password Password
Username is in use
Password doesn't match
Home Page
New Post Box
Some old Posts



If we have time add: Successfully logged out
"""



# TEST SERVER
#filepath = "/styles..css"
#@app.route('/static/<filepath:path>')
#def static_CSS(filepath):
#   return static_file(filepath, root='/static')

hostName = "localhost"
serverPort = 8090  # Changed default port to 8090
login_template = """
<!DOCTYPE HTML>
<html>

<head>
    <meta name="author" content="Cameron Squires">
    <title>Quiz from 2005</title>
</head>

<body>
    <p>
        WELCOME TO HOME PAGE
    </p>
</body>
</html>
"""

html_template = """
<!DOCTYPE HTML>
<html>

<head>
    <meta name="author" content="Cameron Squires">
    <title>Quiz from 2005</title>
</head>

<body>
    <form method="POST" action="/login">
    <div>
        <label for="username">Username</label>
        <input action="" placeholder="Username" id="username"></input>
    </div>
    <div>
        <label for="password">Password</label>
        <input action="" id="password" type = "password" placeholder="Password"></input>
    </div>
    </br>
        <input type="submit" value="Login"></input>
    </form>
</body>
</html>
"""

html_template_failed = """
<!DOCTYPE HTML>
<html>

<head>
    <meta name="author" content="Cameron Squires">
    <title>Quiz from 2005</title>
</head>

<body>
    <form method="POST" action="/login">
    <div>
        <label for="username">Username</label>
        <input action="" placeholder="Username" id="username"></input>
    </div>
    <div>
        <label for="password">Password</label>
        <input action="" id="password" type = "password" placeholder="Password"></input>
    </div>
        <strong>INCORRECT USERNAME OR PASSWORD</strong>
        </br>
        <input type="submit" value="Login"></input>
    </form>
</body>
</html>
"""

class TestServer(Bottle):
    def __init__(self):
        super(TestServer, self).__init__()
        self.route("/", callback=self.testing)
        self.route("/login", callback=self.login, method="POST")
        self.route("/loginfailed", callback=self.loginfailed, method="GET")
        
    def testing(self):
        return html_template

    def login(self):
        return login_template

    def loginfailed(self):
        return html_template_failed


if __name__ == "__main__":
    test = TestServer()
    test.run(host=hostName, port=serverPort, debug=True)