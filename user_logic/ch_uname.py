from bottle import request, redirect
from HTML_Templates.Templates import ch_uname_page
from storage import dataHandler as dH
from .signin import username_available


dataHandler = dH.dataBaseHandler()

def returnTemplate():
    return ch_uname_page.return_template()

def changeUsername(session_data):

    username = request.forms.get('old_username')
    new_username = request.forms.get('new_username')
    retype_new_username = request.forms.get('retype_new_username')
    # Check if the password and retype_password match
    if new_username != retype_new_username:
        return "New Username do not match. <a href='/editUsername'>Try again</a>"
    # Check if the username is already in use
    if not username_available(new_username):
        return "Username already in use. <a href='/editUsername'>Try a different username</a>"
    # Create the user
    dataHandler.setUsername(new_username, dataHandler.getUserID(username))
    # Set the user in the session
    session_data['user'] = new_username
    redirect('/')