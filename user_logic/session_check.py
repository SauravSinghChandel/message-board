from HTML_Templates.Templates import *


def index(session_data):
    if 'user' in session_data:
        return home_template.return_template()
    else:
        return login.return_template()
