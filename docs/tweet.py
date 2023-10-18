from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

# A dictionary to simulate user accounts (username: password)
users = {
    "username1": "password1",
    "username2": "password2"
}

@app.route('/')
def index():
    return "Welcome to the Chat Forum!"

@app.route('/chat/<username>', methods=['GET', 'POST'])
def chat(username):
    if request.method == 'POST':
        message = request.form['message']
        if message.strip() != "":
            # Handle the message (you can save it to a database, etc.)
            return redirect(url_for('chat', username=username))
    
    return render_template('chat.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
