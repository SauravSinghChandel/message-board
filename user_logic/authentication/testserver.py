from bottle import Bottle, request, response
import login

hostName = "localhost"
serverPort = 8090  # Changed default port to 8090

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <form method="POST" action="/login">
        <label for="username">Username:</label>
        <input type="text" name="username" id="username" required><br>
        <label for="password">Password:</label>
        <input type="password" name="password" id="password" required><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
"""

home = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h2>LOGGED IN SUCCESFULLY this is a sample home page</h2>
</body>
</html>
"""


class QuizServer(Bottle):

    def __init__(self):
        super(QuizServer, self).__init__()
        self.route("/", callback=self.index)
        self.route("/login", callback=login.login, method="POST")
        self.route("/home", callback=self.home)

    def index(self):
        return html_template

    def home(self):
        return home


if __name__ == "__main__":
    qs = QuizServer()
    qs.run(host=hostName, port=serverPort, debug=True)

