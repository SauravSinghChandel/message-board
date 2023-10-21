from HTML_Templates.Templates import home_page, login_page


def index(session_data):
    if 'user' in session_data:
        return home_page.return_template()
    else:
        return login_page.return_template()
