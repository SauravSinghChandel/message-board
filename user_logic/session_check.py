from HTML_Templates import *


def index(session_data):
    if 'user' in session_data:
        return home_template
    else:
        return login_template
