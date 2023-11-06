from bottle import request, redirect
from storage import dataHandler as dH
from HTML_Templates.Templates import *
import datetime


dataHandler = dH.dataBaseHandler()

def make_post(session_data):
    date = str(datetime.date.today())
    username = session_data['user']
    content = request.forms.get('post')
    message_id = username + date
    data = [date, username, content, message_id]
    dataHandler.addMessage(data)
    redirect('/')
    
def display_posts():
    res = []
    data = dataHandler.displayTableMessages(1000)
    for message in data:
        res.append(message[2])
    
    return res