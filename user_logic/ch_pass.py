from bottle import request, redirect
from HTML_Templates.Templates import ch_password_page
from storage import dataHandler as dH
from cryptography.fernet import Fernet


key = b'2hX8MUwJ_JDcuQTv2YnwsVcP7Bij3Bw_9KTFkvhDiMc='
fernet = Fernet(key)

dataHandler = dH.dataBaseHandler()

def returnTemplate():
    return ch_password_page.return_template()

def changePassword(session_data):

    username = session_data['user']
    password = request.forms.get('old_password')
    new_password = request.forms.get('new_password')
    retype_new_password = request.forms.get('retype_new_password')
    # Check if the password and retype_password match
    if new_password != retype_new_password:
        return "New Passwords do not match. <a href='/editPassword'>Try again</a>"
    # Check if the username is already in use
    if password != dataHandler.getPassword(dataHandler.getUserID(username)):
        return "The old password does not match. <a href='/editPassword'> Try again</a>"
    # Create the user
    new_password = fernet.encrypt(new_password.encode())
    dataHandler.setPassword(username, new_password)

    redirect('/')