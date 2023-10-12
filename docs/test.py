from bottle import Bottle, request, response
import sys

# TEST SERVER


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
    <form action="/login" method="POST">
        <p>
        <input action="" placeholder="Username"></form>
        <input action="" type = "password" placeholder="Password"></form>
        </br>
        <button type="submit" name="but" value="0" id="0"> Login</button>
        </p>
    </form>
</body>
</html>
"""

class TestServer(Bottle):
    def __init__(self):
        super(TestServer, self).__init__()
        self.route("/", callback=self.testing)
        self.route("/login", callback=self.login, method="POST")
        
    def testing(self):
        return html_template

    def login(self):
        return login_template

if __name__ == "__main__":
    test = TestServer()
    test.run(host=hostName, port=serverPort, debug=True)