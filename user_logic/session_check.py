from HTML_Templates.Templates import home_page, login_page


def index(session_data):
    """
    Display the appropriate page (home page or login page) based on the user's session status.

    Args:
        session_data (dict): The user's session data for session management.

    Returns:
        str: HTML template for the home page if the user is logged in, or the login page if not.
    """
    if 'user' in session_data:
        return home_page.return_template(session_data['user'])
    else:
        return login_page.return_template()
